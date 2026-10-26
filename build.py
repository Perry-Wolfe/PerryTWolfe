"""Build the deployable site/ folder from src/page.html."""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "page.html"
OUT = ROOT / "site"

LINKEDIN = "https://www.linkedin.com/in/perry-wolfe-193a10171/"
INSTAGRAM = "https://www.instagram.com/theperrywolfe/"


def build_index() -> str:
    head, body = SRC.read_text().split("</style>\n", 1)
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        + head + "</style>\n</head>\n<body>\n" + body + "</body>\n</html>\n"
    )


VCARD = "\r\n".join([
    "BEGIN:VCARD",
    "VERSION:3.0",
    "N:Wolfe;Perry;T.;;",
    "FN:Perry T. Wolfe",
    "ORG:Wolfe Worldwide",
    "TITLE:Founder & CEO",
    "TEL;TYPE=CELL,VOICE:+1-915-820-1384",
    "EMAIL;TYPE=INTERNET,WORK:perry@wolfeworldwide.com",
    "URL:https://perrytwolfe.com",
    "X-SOCIALPROFILE;TYPE=instagram:" + INSTAGRAM,
    "X-SOCIALPROFILE;TYPE=linkedin:" + LINKEDIN,
    "NOTE:Founder & CEO of RunTorque\\, Needset AI and SXRX Health.",
    "END:VCARD",
]) + "\r\n"

HEADERS = """/perry-wolfe.vcf
  Content-Type: text/vcard; charset=utf-8
  Content-Disposition: attachment; filename="Perry-Wolfe.vcf"

/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: DENY
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Permissions-Policy: camera=(), microphone=(), geolocation=()
"""

REDIRECTS = """https://www.perrytwolfe.com/* https://perrytwolfe.com/:splat 301!
"""

ROBOTS = "User-agent: *\nAllow: /\nSitemap: https://perrytwolfe.com/sitemap.xml\n"

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://perrytwolfe.com/</loc><lastmod>2026-10-26</lastmod></url>
</urlset>
"""

THANKS = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Perry T. Wolfe</title>
<style>
body{margin:0;min-height:100vh;display:grid;place-items:center;background:#0D1220;color:#E8EBF2;font:17px/1.6 system-ui,-apple-system,sans-serif;padding:24px}
h1{font-size:40px;line-height:1;margin:0 0 12px}
a{color:#F4B740}
</style>
</head>
<body>
<main>
<h1>You're on the list.</h1>
<p>Watch for a note from perry@wolfeworldwide.com.</p>
<p><a href="/">Back to perrytwolfe.com</a></p>
</main>
</body>
</html>
"""

NOT_FOUND = THANKS.replace("You're on the list.", "Page not found.").replace(
    "<p>Watch for a note from perry@wolfeworldwide.com.</p>\n", "")

NETLIFY_TOML = """[build]
  publish = "site"
"""


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(build_index())
    (OUT / "perry-wolfe.vcf").write_bytes(VCARD.encode("utf-8"))
    (OUT / "_headers").write_text(HEADERS)
    (OUT / "_redirects").write_text(REDIRECTS)
    (OUT / "robots.txt").write_text(ROBOTS)
    (OUT / "sitemap.xml").write_text(SITEMAP)
    (OUT / "thanks.html").write_text(THANKS)
    (OUT / "404.html").write_text(NOT_FOUND)
    (ROOT / "netlify.toml").write_text(NETLIFY_TOML)


if __name__ == "__main__":
    main()
