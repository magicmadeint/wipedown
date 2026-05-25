import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Updated active Nitter-style instances (May 2026)
NITTER_INSTANCES = [
    "xcancel.com",           # Currently one of the most reliable
    "nitter.poast.org",
    "nitter.privacydev.net",
    "nitter.tiekoetter.com",
    "nitter.catsarch.com",
    "nitter.kareem.one",
    "nitter.privacyredirect.com",
]

def get_scrape_targets(url: str) -> list[str]:
    """Generate fallback URLs for JS-heavy platforms (X/Twitter)."""
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    targets = []

    if domain in ["x.com", "twitter.com", "www.x.com", "www.twitter.com"]:
        for instance in NITTER_INSTANCES:
            new_url = url.replace(parsed.netloc, instance)
            # Most instances (including xcancel) work best without the extra /i/
            if "/i/status/" in new_url:
                new_url = new_url.replace("/i/status/", "/status/")
            targets.append(new_url)
    else:
        targets.append(url)
        
    return targets

def structural_strip(html: str) -> str:
    """Stage 1: Forcefully strip everything that isn't visible semantic prose."""
    soup = BeautifulSoup(html, "html.parser")
    
    for tag in soup(["script", "style", "iframe", "noscript", "svg", "meta", "link", "header", "footer", "nav"]):
        tag.decompose()
    
    for tag in soup.find_all(style=re.compile(r'display:\s*none|visibility:\s*hidden', re.I)):
        tag.decompose()
    
    text = soup.get_text(separator="\n", strip=True)
    text = re.sub(r'[\u200B-\u200D\uFEFF\u2028\u2029\u00A0]', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    return text.strip()