import os
import yaml
from mkdocs.structure.pages import Page

def on_page_markdown(markdown: str, page: Page, config, files):
    # Only modify the ADR index page
    if not page.file.src_path.startswith("adrs/index.md"):
        return markdown

    adrs = []
    docs_dir = config["docs_dir"]
    adrs_dir = os.path.join(docs_dir, "adrs")

    for filename in sorted(os.listdir(adrs_dir)):
        if filename.endswith(".md") and filename != "index.md":
            with open(os.path.join(adrs_dir, filename), "r") as f:
                content = f.read()
                if content.startswith("---"):
                    _, fm, body = content.split("---", 2)
                    meta = yaml.safe_load(fm)
                    adrs.append({
                        "file": filename,
                        "title": extract_title(body) or filename,
                        "status": meta.get("status", "unknown"),
                        "date": meta.get("date", "n/a")
                    })

    table = [
        "| ADR | Status | Date |",
        "|-----|---------|------|",
    ]
    for adr in adrs:
        link = f"[{adr['title']}]({adr['file']})"
        table.append(f"| {link} | {adr['status']} | {adr['date']} |")

    return markdown + "\n\n" + "\n".join(table)

def extract_title(body):
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None
