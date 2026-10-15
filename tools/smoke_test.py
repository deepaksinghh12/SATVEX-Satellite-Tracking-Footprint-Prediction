import os
import sys
import urllib.request

base_url = os.environ.get("BASE_URL", "http://localhost:8000").rstrip("/")
urls = [
    f'{base_url}/healthz',
    f'{base_url}/',
    f'{base_url}/sat',
    f'{base_url}/about',
    f'{base_url}/pass-predictor',
    f'{base_url}/multi-viewer',
    f'{base_url}/comparison',
    f'{base_url}/tle-comparison',
    f'{base_url}/test-bhuvan',
    f'{base_url}/api/satellites/list',
    f'{base_url}/static/css/home.css',
]

print(f"Running smoke tests against: {base_url}")
failed = False
for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'satvex-smoke-test/1.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            print(f"[PASS] {u} -> {r.status} {r.getheader('Content-Type')!s}")
    except Exception as e:
        print(f"[FAIL] {u} -> ERROR: {e}")
        failed = True

if failed:
    sys.exit(1)
else:
    print("All smoke test routes passed successfully.")

