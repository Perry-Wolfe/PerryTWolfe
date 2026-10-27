# perrytwolfe.com

Personal site for Perry T. Wolfe.

- `src/page.html` is the single source for the page (styles, markup and script).
- `build.py` writes the deployable `site/` folder: `index.html`, the contact card (`perry-wolfe.vcf`), headers, redirects, sitemap, robots, thank-you and 404 pages.
- Run `python3 build.py` after editing `src/`, then commit both `src/` and `site/`. Netlify publishes `site/` as is on every push to `main`, with no build step.
- The "Get updates" signup uses Netlify Forms (form name `updates`). Submissions appear under Forms in the Netlify project.

Local build:

```
python3 build.py
```
