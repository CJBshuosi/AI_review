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

def run_review(diff, context_snippets):
    prompt = REVIEW_PROMPT.format(patch=diff, context_snippets=context_snippets)
    review_text = ask_model(prompt)
    return review_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--pr", type=int, required=True)
    args = parser.parse_args()

    token = os.getenv("GITHUB_TOKEN")
    diff = get_pr_diff(args.repo, args.pr, token)

    # TODO: 可以用 RAG 检索上下文文档
    context_snippets = ""  # 先留空或加载 knowledge/*.md

    review_text = run_review(diff, context_snippets)
    comment_body = f"### 🤖 AI Code Review Report\n\n{review_text}"
    post_comment(args.repo, args.pr, token, comment_body)
