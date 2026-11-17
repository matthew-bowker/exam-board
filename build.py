#!/usr/bin/env python3
"""Pack src/app.html into index.html.

index.html is a self-contained page. The app (markup, styles and the model's
JavaScript) is stored as a JSON string inside <script type="__bundler/template">,
and React, the page runtime and the Rubik font are stored, compressed, inside
<script type="__bundler/manifest">. When the page opens, its loader unpacks them.

To change the game, edit src/app.html and run:

    python3 build.py

This replaces only the app inside index.html; the packed libraries and font are
kept as they are. In src/app.html, leave the long IDs such as
"35b626f5-fd93-419a-a027-a70eeee01349" unchanged: the loader swaps each one for
the packed file it names.
"""
import json
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent
app = (root / "src" / "app.html").read_text(encoding="utf-8")
page_path = root / "index.html"
page = page_path.read_text(encoding="utf-8")

block = re.compile(r'(<script type="__bundler/template">\n)(.*?)(\n  </script>)', re.S)
if not block.search(page):
    sys.exit("Could not find the app template block in index.html.")

# Same encoding as the original export: plain UTF-8 JSON, with "</" escaped so
# the string cannot close the surrounding <script> tag early.
encoded = json.dumps(app, ensure_ascii=False).replace("</", "<\\u002F")
page = block.sub(lambda m: m.group(1) + encoded + m.group(3), page, count=1)
page_path.write_text(page, encoding="utf-8")
print(f"Wrote index.html ({len(page.encode('utf-8')) / 1024:.0f} KB)")
