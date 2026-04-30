import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the h1 with either curly or straight apostrophe
pattern = r"      <h1>Gagnez de <span class=\"accent\">l.argent avec vos id\u00e9es -</span> depuis votre t\u00e9l\u00e9phone</h1>"
new_h1 = (
    '      <h1>Rejoignez le r\u00e9seau des <span class="accent">administrateurs id\u00e9ateurs</span></h1>\n'
    '      <p class="hero-support">Participez au d\u00e9veloppement de projets concrets</p>'
)

result, n = re.subn(pattern, new_h1, content, count=1)
if n:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"SUCCESS: replaced {n} occurrence(s)")
else:
    print("NOT FOUND - dumping h1 lines:")
    for i, line in enumerate(content.splitlines(), 1):
        if '<h1>' in line:
            print(f"  line {i}: {repr(line)}")
