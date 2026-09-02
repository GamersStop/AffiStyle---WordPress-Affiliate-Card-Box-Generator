import glob
import re
import json

def clean_text(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    return ' '.join(text.split())

def analyze_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
    title = clean_text(title_match.group(1)) if title_match else ''
    
    meta_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.DOTALL | re.IGNORECASE)
    meta = clean_text(meta_match.group(1)) if meta_match else ''
    
    h1_matches = [clean_text(m.group(1)) for m in re.finditer(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)]
    h2_matches = [clean_text(m.group(1)) for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL | re.IGNORECASE)]
    h3_matches = [clean_text(m.group(1)) for m in re.finditer(r'<h3[^>]*>(.*?)</h3>', html, re.DOTALL | re.IGNORECASE)]
    
    # Check for layout-fix passage
    passage_match = re.search(r'class=["\']layout-fix-passage["\'][^>]*>(.*?)</p>', html, re.DOTALL)
    passage = clean_text(passage_match.group(1)) if passage_match else ''
    
    # Check for Schema JSON-LD
    schema_match = re.search(r'<script type=["\']application/ld\+json["\']>(.*?)</script>', html, re.DOTALL)
    schema_data = None
    if schema_match:
        try:
            schema_data = json.loads(schema_match.group(1))
        except Exception as e:
            schema_data = f'Error parsing: {e}'
            
    return {
        'file': filepath,
        'title': title,
        'meta_description': meta,
        'h1': h1_matches,
        'h2': h2_matches,
        'h3': h3_matches,
        'layout_fix_passage': passage,
        'schema': schema_data
    }

print("=== BLOG POSTS H1 VERIFICATION ===")
for path in sorted(glob.glob('blog/*.html')):
    b = analyze_html(path)
    print(f"File: {path}")
    print(f"  H1 Count: {len(b['h1'])}")
    print(f"  H1 Text: {b['h1']}")

keywords_to_check = [
    "Amazon Associates",
    "AAWP",
    "Lasso",
    "Pretty Links",
    "affiliate box",
    "Gutenberg",
    "CLS",
    "layout shift",
    "FTC",
    "link cloaking"
]

with open('index.html', 'r', encoding='utf-8') as f:
    full_html = f.read().lower()

print("\n=== KEYWORD OCCURRENCE IN INDEX.HTML ===")
for kw in keywords_to_check:
    count = len(re.findall(re.escape(kw.lower()), full_html))
    print(f"{kw}: {count}")

# Check schema JSON-LD specifically for new entities
m = re.search(r'<script type=["\']application/ld\+json["\']>(.*?)</script>', full_html, re.DOTALL)
if m:
    schema_str = m.group(1)
    print("\n=== SCHEMA.ORG JSON-LD CHECK ===")
    for kw in ["aawp", "lasso", "pretty links"]:
        print(f"'{kw}' in JSON-LD: {kw in schema_str}")
