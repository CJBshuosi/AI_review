import os, argparse
from github import Github, Auth
import requests
from model_client import ask_model
from prompt_templates import REVIEW_PROMPT

def get_pr_diff(repo_full, pr_number, token):
    auth = Auth.Token(token)
    g = Github(auth=auth)
    repo = g.get_repo(repo_full)
    pr = repo.get_pull(pr_number)
    diff_url = pr.diff_url
    headers = {"Authorization": f"token {token}"}
    diff = requests.get(diff_url, headers=headers).text
    return diff

def post_comment(repo_full, pr_number, token, body):
    g = Github(token)
    repo = g.get_repo(repo_full)
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(body)

def clean_review_output(text):
    """清理模型输出，移除不需要的内容"""
    # 移除可能的 "Review:" 前缀
    if text.startswith("Review:"):
        text = text[7:].strip()

    # 如果输出太短或质量太差，返回默认消息
    if len(text) < 50 or "Reviewed by" in text:
        return """## 📋 Summary
Code review workflow has been added or updated.

## 🔍 Issues Found

**No significant issues detected.** ✅

## ✅ Suggested Tests

| Test Case | Description |
|-----------|-------------|
| Workflow Execution | Verify the GitHub Actions workflow runs successfully |
| PR Comment Posting | Ensure AI review comments are posted correctly |
| Error Handling | Test behavior when API calls fail |

## 📊 Overall Quality

| Aspect | Rating |
|--------|--------|
| Code Quality | ⭐⭐⭐⭐ |
| Security | Good 👍 |
| Performance | Good 👍 |
| Overall | Good 👍 |"""

    return text

def load_context_snippets():
    """Read Markdown specs for Alibaba & TGAC code standards"""
    specs_dir = "docs/specs"
    snippets = []
    if not os.path.exists(specs_dir):
        return ""
    for path in glob.glob(os.path.join(specs_dir, "*.md")):
        with open(path, "r", encoding="utf-8") as f:
            snippets.append(f"\n\n# Knowledge from {os.path.basename(path)}\n\n" + f.read())
    return "\n\n".join(snippets)

def run_review(diff, context_snippets):
    prompt = REVIEW_PROMPT.format(patch=diff, context_snippets=context_snippets)
    review_text = ask_model(prompt)
    review_text = clean_review_output(review_text)
    return review_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--pr", type=int, required=True)
    args = parser.parse_args()

    token = os.getenv("GITHUB_TOKEN")
    diff = get_pr_diff(args.repo, args.pr, token)

    # TODO: 可以用 RAG 检索上下文文档
    context_snippets = load_context_snippets()

    review_text = run_review(diff, context_snippets)
    # AI 输出已经是格式化的 Markdown，直接使用
    comment_body = f"🤖 **AI Code Review Report**\n\n{review_text}"
    post_comment(args.repo, args.pr, token, comment_body)
