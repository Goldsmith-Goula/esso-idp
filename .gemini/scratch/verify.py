with open('index.html', encoding='utf-8') as f:
    content = f.read()

checks = [
    ('h1 new headline',           'administrateurs id'),
    ('hero-support class',        'hero-support'),
    ('project-cta section',       'project-cta'),
    ('wa.me admin link',          'wa.me/237681335213'),
    ('project WA link',           'porteur%20de%20projet'),
    ('expansion section',         'expansion'),
    ('plateforme en expansion',   'plateforme en expansion'),
]

all_ok = True
for label, keyword in checks:
    ok = keyword in content
    status = 'OK' if ok else 'MISSING'
    print(f"  [{status}] {label}")
    if not ok:
        all_ok = False

print()
print("All checks passed!" if all_ok else "Some checks FAILED.")
