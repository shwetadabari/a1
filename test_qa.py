import os
import re
import json
import hashlib
from html.parser import HTMLParser

SITE_DIR = r"d:\antigravity website\risottogarden"
EXPECTED_ADDR = "601 Union Street, Suite 4200, Seattle, WA 98101, United States"
EXPECTED_PHONE = "+1-888-924-4195"
GA_TAG = "G-0LY0HY7L01"

class SimpleTagExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headers = []
        self.drawers = []
        self.imgs = []
        self.policy_paras = []
        self._current_tag = None
        self._current_attrs = {}
        self._capture_text = False
        self._buffer = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self._current_tag = tag
        self._current_attrs = attr_dict

        if tag == "header" and "site-header" in attr_dict.get("class", ""):
            self.headers.append(attr_dict)
        if tag == "div" and attr_dict.get("id") == "mobile-drawer":
            self.drawers.append(attr_dict)
        if tag == "img":
            self.imgs.append(attr_dict)
        if tag == "p" and "rg-policy-p" in attr_dict.get("class", ""):
            self._capture_text = True
            self._buffer = []

    def handle_data(self, data):
        if self._capture_text:
            self._buffer.append(data)

    def handle_endtag(self, tag):
        if tag == "p" and self._capture_text:
            self._capture_text = False
            self.policy_paras.append(" ".join(self._buffer).strip())
            self._buffer = []

def run_qa():
    print("=" * 60)
    print("STARTING RIGOROUS QA AUDIT FOR RISOTTOGARDEN")
    print("=" * 60)
    passed = 0
    total = 0

    def assert_check(name, condition, details=""):
        nonlocal passed, total
        total += 1
        if condition:
            print(f"[PASS] {name}")
            passed += 1
        else:
            print(f"[FAIL] {name} - {details}")

    # 1. Zero PHP files
    php_files = []
    for root, dirs, files in os.walk(SITE_DIR):
        for f in files:
            if f.lower().endswith(".php"):
                php_files.append(os.path.join(root, f))
    assert_check("Zero PHP files allowed (Rule 3)", len(php_files) == 0, f"Found PHP files: {php_files}")

    # 2. Homepage MUST be index.html
    index_path = os.path.join(SITE_DIR, "index.html")
    assert_check("Homepage is index.html (Rule 3)", os.path.exists(index_path))

    # 3. All 9 mandatory HTML pages exist
    mandatory_pages = [
        "index.html", "about.html", "services.html", "contact.html", "faq.html",
        "privacy-policy.html", "terms-and-conditions.html", "disclaimer.html", "cookie-policy.html"
    ]
    for p in mandatory_pages:
        assert_check(f"Page exists: {p}", os.path.exists(os.path.join(SITE_DIR, p)))

    # 4. Strict NO BLOG policy (Rule 4)
    blog_issues = []
    for p in mandatory_pages:
        fp = os.path.join(SITE_DIR, p)
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read().lower()
                if "blog.html" in content or 'href="/blog"' in content or 'class="blog' in content:
                    blog_issues.append(f"{p} has blog link/class")
    assert_check("Strict NO BLOG compliance (Rule 4)", len(blog_issues) == 0, f"Issues: {blog_issues}")

    # 5. Google Analytics Tag in all pages (Rule 2)
    ga_missing = []
    for p in mandatory_pages:
        fp = os.path.join(SITE_DIR, p)
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                c = f.read()
                if GA_TAG not in c or "googletagmanager.com/gtag/js" not in c:
                    ga_missing.append(p)
    assert_check("Google Analytics tag G-0LY0HY7L01 in all pages (Rule 2)", len(ga_missing) == 0, f"Missing: {ga_missing}")

    # 6. Header and Mobile Drawer standards (Rule 11)
    header_drawer_errors = []
    for p in mandatory_pages:
        fp = os.path.join(SITE_DIR, p)
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                parser = SimpleTagExtractor()
                parser.feed(f.read())
                if len(parser.headers) != 1:
                    header_drawer_errors.append(f"{p} has {len(parser.headers)} site-header tags (expected 1)")
                if len(parser.drawers) != 1:
                    header_drawer_errors.append(f"{p} has {len(parser.drawers)} mobile-drawer divs (expected 1)")
    assert_check("Exactly 1 header and 1 mobile drawer per page (Rule 11)", len(header_drawer_errors) == 0, f"Errors: {header_drawer_errors}")

    # 7. Index.html has at least 10 meaningful sections (Rule 6)
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
        sections = re.findall(r'<(?:section|div)[^>]*class=["\'][^"\']*(?:rg-hero|rg-menu-ribbon|rg-section)[^"\']*["\']', content)
        assert_check("Homepage has >= 10 meaningful sections (Rule 6)", len(sections) >= 10, f"Found {len(sections)} sections")

    # 8. Policy Pages word count standard (Rule 5: strictly 60 to 110 words per substantive paragraph)
    policy_pages = ["privacy-policy.html", "terms-and-conditions.html", "disclaimer.html", "cookie-policy.html"]
    policy_errors = []
    total_policy_paras = 0
    for pp in policy_pages:
        fp = os.path.join(SITE_DIR, pp)
        with open(fp, "r", encoding="utf-8") as f:
            parser = SimpleTagExtractor()
            parser.feed(f.read())
            for i, p_text in enumerate(parser.policy_paras):
                total_policy_paras += 1
                words = len(p_text.split())
                if words < 60 or words > 110:
                    policy_errors.append(f"{pp} para {i+1} has {words} words (expected 60-110)")
    assert_check(f"Policy pages substantive paragraphs line count (60-110 words) - Checked {total_policy_paras} paras", len(policy_errors) == 0, f"Errors: {policy_errors}")

    # 9. Unique Institutional Contact Information (Rule 1)
    contact_errors = []
    for pp in policy_pages:
        fp = os.path.join(SITE_DIR, pp)
        with open(fp, "r", encoding="utf-8") as f:
            text = f.read()
            if EXPECTED_ADDR not in text:
                contact_errors.append(f"{pp} missing address")
            if EXPECTED_PHONE not in text:
                contact_errors.append(f"{pp} missing phone")
    assert_check("Unique address and phone in all policy pages (Rule 1)", len(contact_errors) == 0, f"Errors: {contact_errors}")

    # 10. Image verification (Rule 8: Exactly 20 images, >20KB each, used EXACTLY ONCE, 0 duplicates)
    img_dir = os.path.join(SITE_DIR, "assets", "images")
    imgs = [f for f in os.listdir(img_dir) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]
    assert_check("Exactly 20 local images generated (Rule 8)", len(imgs) == 20, f"Found {len(imgs)} images")

    size_errors = []
    hashes = {}
    for img in imgs:
        fp = os.path.join(img_dir, img)
        sz = os.path.getsize(fp)
        if sz <= 20000:
            size_errors.append(f"{img} is {sz} bytes (<= 20KB)")
        with open(fp, "rb") as f:
            h = hashlib.md5(f.read()).hexdigest()
        if h in hashes:
            size_errors.append(f"{img} duplicate hash with {hashes[h]}")
        hashes[h] = img
    assert_check("All 20 images > 20KB each and zero duplicate hashes (Rule 8)", len(size_errors) == 0, f"Errors: {size_errors}")

    # 11. Strict Zero Image Repetition: Every image used EXACTLY ONCE across the entire website
    image_usage_counts = {img: 0 for img in imgs}
    for p in mandatory_pages:
        fp = os.path.join(SITE_DIR, p)
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                parser = SimpleTagExtractor()
                parser.feed(f.read())
                for attr_dict in parser.imgs:
                    src = attr_dict.get("src", "")
                    base = os.path.basename(src)
                    if base in image_usage_counts:
                        image_usage_counts[base] += 1

    zero_rep_errors = []
    for img, count in image_usage_counts.items():
        if count != 1:
            zero_rep_errors.append(f"{img} used {count} times (MUST BE EXACTLY 1)")
    assert_check("Strict Zero Image Repetition (Every image used EXACTLY ONCE) (Rule 8)", len(zero_rep_errors) == 0, f"Errors: {zero_rep_errors}")

    # 12. Rule 13: Ban on house and building images & content
    ban_terms = ["house", "building", "facade", "apartment", "real estate", "residence", "campus", "tower"]
    ban_violations = []
    for p in mandatory_pages:
        fp = os.path.join(SITE_DIR, p)
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                parser = SimpleTagExtractor()
                parser.feed(f.read())
                for attr_dict in parser.imgs:
                    alt = attr_dict.get("alt", "").lower()
                    for bt in ban_terms:
                        if bt in alt:
                            ban_violations.append(f"{p} img alt contains '{bt}': {alt}")
    assert_check("Strict Ban on House & Building imagery (Rule 13)", len(ban_violations) == 0, f"Violations: {ban_violations}")

    # 13. CSS & JS assets exist and non-empty
    css_fp = os.path.join(SITE_DIR, "assets", "css", "style.css")
    js_fp = os.path.join(SITE_DIR, "assets", "js", "script.js")
    main_js_fp = os.path.join(SITE_DIR, "assets", "js", "main.js")
    assert_check("style.css exists and > 5KB", os.path.exists(css_fp) and os.path.getsize(css_fp) > 5000)
    assert_check("script.js exists and > 500B", os.path.exists(js_fp) and os.path.getsize(js_fp) > 500)
    assert_check("main.js exists and > 500B", os.path.exists(main_js_fp) and os.path.getsize(main_js_fp) > 500)

    # 14. Registries & sitemap exist
    for reg in ["sitemap.xml", "robots.txt", "IMAGE_REGISTRY.md", "DESIGN_REGISTRY.md", "SITE_MANIFEST.json"]:
        rfp = os.path.join(SITE_DIR, reg)
        assert_check(f"Registry/Metadata exists: {reg}", os.path.exists(rfp) and os.path.getsize(rfp) > 20)

    print("=" * 60)
    print(f"AUDIT COMPLETED: {passed}/{total} CHECKS PASSED ({passed*100//total}%)")
    print("=" * 60)
    return passed == total

if __name__ == "__main__":
    success = run_qa()
    exit(0 if success else 1)
