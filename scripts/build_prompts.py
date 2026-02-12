import os
import re
import yaml
from collections import defaultdict

CATEGORY_TO_PATH = {
    "Programming & Tech": "main_base/purpose/programming.md",
    "Writing & Content": "main_base/purpose/writing.md",
    "Marketing, SEO & Growth": "main_base/purpose/marketing.md",
    "Business & Strategy": "main_base/purpose/business.md",
    "Productivity & Workflow": "main_base/purpose/productivity.md",
    "Education & Learning": "main_base/purpose/education.md",
    "Career & Hiring": "main_base/purpose/career.md",
    "Customer Support & Success": "main_base/purpose/customer_support.md",
}

ORDERED_CATEGORIES = [
    "Programming & Tech",
    "Writing & Content",
    "Marketing, SEO & Growth",
    "Business & Strategy",
    "Productivity & Workflow",
    "Education & Learning",
    "Career & Hiring",
    "Customer Support & Success",
]

def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_-]+", "-", s)
    return s.strip("-")

def md_escape(s: str) -> str:
    return s.replace("\r\n", "\n").strip()

def ensure_dir(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

def load_prompts(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    if not isinstance(data, list):
        raise ValueError("prompts.yaml must be a list")
    for p in data:
        for k in ["id", "title", "category", "prompt"]:
            if k not in p or not str(p[k]).strip():
                raise ValueError(f"Prompt missing required field: {k}")
    ids = [p["id"] for p in data]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate prompt id found")
    return data

def render_prompt_block(p: dict) -> str:
    lines = []
    lines.append(f"## {md_escape(p['title'])}\n\n")
    meta = []
    if p.get("difficulty"):
        meta.append(("Difficulty", md_escape(str(p["difficulty"]))))
    if p.get("tags"):
        meta.append(("Tags", ", ".join([md_escape(str(x)) for x in p["tags"]])))
    if p.get("best_for"):
        meta.append(("Best for", ", ".join([md_escape(str(x)) for x in p["best_for"]])))
    if p.get("output"):
        meta.append(("Output", ", ".join([md_escape(str(x)) for x in p["output"]])))
    if meta:
        for k, v in meta:
            lines.append(f"**{k}:** {v}\n\n")
    lines.append("**Prompt:**\n\n")
    lines.append("```text\n")
    lines.append(md_escape(p["prompt"]) + "\n")
    lines.append("```\n\n")
    return "".join(lines)

def write_category_pages(prompts):
    by_cat = defaultdict(list)
    unknown = []
    for p in prompts:
        cat = p["category"]
        if cat not in CATEGORY_TO_PATH:
            unknown.append(cat)
            continue
        by_cat[cat].append(p)

    for cat in ORDERED_CATEGORIES:
        path = CATEGORY_TO_PATH[cat]
        ensure_dir(path)
        items = by_cat.get(cat, [])
        items = sorted(items, key=lambda x: (x.get("difficulty", ""), x["title"].lower()))
        out = []
        out.append(f"# {cat}\n\n")
        out.append("High-quality prompts curated for this purpose.\n\n")
        out.append("## Index\n\n")
        if items:
            for p in items:
                out.append(f"- [{md_escape(p['title'])}](#{slugify(p['title'])})\n")
        else:
            out.append("- (No prompts yet)\n")
        out.append("\n---\n\n")
        for p in items:
            out.append(render_prompt_block(p))
        with open(path, "w", encoding="utf-8") as f:
            f.write("".join(out))

    if unknown:
        unknown_unique = sorted(set(unknown))
        raise ValueError("Unknown categories in prompts.yaml: " + ", ".join(unknown_unique))

def write_master_page(prompts):
    out = []
    out.append("# Prompt Index\n\n")
    out.append("Single source index generated from `data/prompts.yaml`.\n\n")
    by_cat = defaultdict(list)
    for p in prompts:
        by_cat[p["category"]].append(p)
    out.append("## Categories\n\n")
    for cat in ORDERED_CATEGORIES:
        out.append(f"- {cat}\n")
    out.append("\n---\n\n")
    for cat in ORDERED_CATEGORIES:
        out.append(f"## {cat}\n\n")
        items = sorted(by_cat.get(cat, []), key=lambda x: x["title"].lower())
        if not items:
            out.append("- (No prompts yet)\n\n")
            continue
        for p in items:
            out.append(f"- **{md_escape(p['title'])}** (`{p['id']}`)\n")
        out.append("\n")
    with open("PROMPTS.md", "w", encoding="utf-8") as f:
        f.write("".join(out))

def main():
    prompts = load_prompts("data/prompts.yaml")
    write_category_pages(prompts)
    write_master_page(prompts)

if __name__ == "__main__":
    main()
