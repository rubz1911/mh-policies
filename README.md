# DOCX Knowledge Library — GitHub Pages

A zero-backend, GitHub Pages–hosted reference library for `.docx` files. Add files via the GitHub web UI; an Action generates a machine-readable `index.json` your copilot/agent can read.

## How it works
- Static site (no server). Everything in this repo is served by GitHub Pages.
- Place your `.docx` files in `library/` (via GitHub "Upload files" button).
- A GitHub Action updates `index.json` on every push using `build_index.py`.
- Your agent hits `https://<user>.github.io/<repo>/index.json` to enumerate files.

## Quick start
1. Create a **new GitHub repo** (public or private with Pages enabled).
2. Download this starter ZIP and push contents, or upload via GitHub UI.
3. Commit and push.
4. Enable **GitHub Pages**: Settings → Pages → Build from branch: `main` / root.
5. Visit your site: `https://<user>.github.io/<repo>/`
6. Upload `.docx` into `library/`. Wait for the GitHub Action to finish.
7. Confirm the machine index at: `https://<user>.github.io/<repo>/index.json`.

## Notes
- File size: keep `.docx` reasonably small (<25–50 MB). Avoid Git LFS for Pages.
- Security: This is a public library if your repo is public. Use a **private** repo + Pages if your org allows, or a dedicated public repo containing only safe docs.
- The site does **not** parse `.docx` contents (good for restricted laptops). If you want extracted text, pre-process locally and commit `.txt` alongside.
- If your Pages URL uses a custom domain, paths still work the same.

## Agent tips
Each item in `index.json` looks like:
```json
{
  "name": "Policy.docx",
  "stem": "Policy",
  "size_bytes": 12345,
  "last_modified": "2025-10-14T21:10:00+00:00",
  "url": "./library/Policy.docx"
}
```
Your agent can:
- Fetch `index.json`
- Loop over items and `GET` `url` to download the file
- Cache `last_modified` to detect updates
