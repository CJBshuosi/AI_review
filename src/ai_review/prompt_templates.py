REVIEW_PROMPT = """Analyze this code change and provide a code review.

Code changes:
{patch}

Context:
{context_snippets}

Write a code review in this exact format:

## 📋 Summary
[2-3 sentences about what changed]

## 🔍 Issues Found
[List issues with 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW severity, or write "No significant issues detected. ✅"]

## ✅ Suggested Tests
[List 2-3 test cases]

## 📊 Overall Quality
[Write: Good 👍 OR Needs Improvement ⚠️ OR Critical Issues 🚨]

Important: Do NOT include code snippets or file paths in your review. Only describe the issues and suggestions."""
