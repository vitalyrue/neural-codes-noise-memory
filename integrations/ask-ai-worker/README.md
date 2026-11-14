# Shared Ask AI service

This book uses the same Cloudflare Worker as the performance engineering books. The Worker in this directory is based on `website/ask-ai/backend` in the performance engineering course, with narrowly scoped additions for this book's GitHub Pages and Tailscale addresses. The selection UI is in `assets/reading-actions` and is attached during `verification/publish_assets.py`.

The service retains the course's existing global and per-IP quotas; this book and the other books share that capacity. CORS and page checks are not authentication. Questions send selected text and nearby section text to the service. Reports open a GitHub issue draft in this book's repository; the reader decides whether to submit it.

The Worker copy and the course's backend must be kept synchronized. Before deploying either one, compare the files and retain both sets of allowed paths; deploying an older course copy would remove support for this book. Run `node --test integrations/ask-ai-worker/worker.test.mjs` and a Wrangler dry run before deploying. The last course-only production version before this integration was `97b8920d-886a-4db5-b599-9aea9ff7e269`; rolling back to it disables Ask AI for this book.
