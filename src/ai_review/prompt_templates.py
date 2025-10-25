REVIEW_PROMPT = """Analyze this code change and provide a code review.

Code changes:
{patch}

Context:
{context_snippets}

Write a code review in this EXACT format with Markdown tables:

## 📋 Summary
[Write 2-3 sentences describing what changed]

## 🔍 Issues Found

| Severity | Issue | Suggestion |
|----------|-------|------------|
| 🔴 HIGH | [Describe critical issue] | [How to fix it] |
| 🟡 MEDIUM | [Describe moderate issue] | [How to fix it] |
| 🟢 LOW | [Describe minor issue] | [How to fix it] |

If no issues found, write: **No significant issues detected.** ✅

## ✅ Suggested Tests

| Test Case | Description |
|-----------|-------------|
| Test 1 | [What to test] |
| Test 2 | [What to test] |
| Test 3 | [What to test] |

## 📊 Overall Quality

| Aspect | Rating |
|--------|--------|
| Code Quality | ⭐⭐⭐⭐⭐ (1-5 stars) |
| Security | Good 👍 / Needs Review ⚠️ / Critical 🚨 |
| Performance | Good 👍 / Needs Review ⚠️ / Critical 🚨 |
| Overall | Good 👍 / Needs Improvement ⚠️ / Critical Issues 🚨 |

Important: Use ONLY tables. Do NOT include code snippets or file paths."""
