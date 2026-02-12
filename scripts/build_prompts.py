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

    "Image Prompts (General)": "main_base/purpose/image_general.md",
    "Product & E-commerce": "main_base/purpose/image_product.md",
    "Logos & Branding": "main_base/purpose/image_branding.md",
    "Illustration & Concept Art": "main_base/purpose/image_concept_art.md",
    "Photography Styles & Lighting": "main_base/purpose/image_photography.md",

    "Video Prompts (General)": "main_base/purpose/video_general.md",
    "Storyboards & Shot Lists": "main_base/purpose/video_storyboard.md",
    "Ads & Social Clips": "main_base/purpose/video_ads.md",
    "Cinematic Styles & Camera Moves": "main_base/purpose/video_cinematic.md",

    "Music Prompts (General)": "main_base/purpose/music_general.md",
    "Genres, Mood & Structure": "main_base/purpose/music_genres.md",
    "Lyrics & Songwriting": "main_base/purpose/music_lyrics.md",
    "Sound Effects (SFX)": "main_base/purpose/audio_sfx.md",

    "Voice Prompts (General)": "main_base/purpose/voice_general.md",
    "Voiceovers & Narration": "main_base/purpose/voiceover.md",
    "Characters & Acting": "main_base/purpose/voice_characters.md",
    "Dubbing & Localization": "main_base/purpose/voice_dubbing.md",
}

NAVIGATION_ORDER = [
    "Programming & Tech",
    "Writing & Content",
    "Marketing, SEO & Growth",
    "Business & Strategy",
    "Productivity & Workflow",
    "Education & Learning",
    "Career & Hiring",
    "Customer Support & Success",

    "Image Prompts (General)",
    "Product & E-commerce",
    "Logos & Branding",
    "Illustration & Concept Art",
    "Photography Styles & Lighting",

    "Video Prompts (General)",
    "Storyboards & Shot Lists",
    "Ads & Social Clips",
    "Cinematic Styles & Camera Moves",

    "Music Prompts (General)",
    "Genres, Mood & Structure",
    "Lyrics & Songwriting",
    "Sound Effects (SFX)",

    "Voice Prompts (General)",
    "Voiceovers & Narration",
    "Characters & Acting",
    "Dubbing & Localization",
]

def slugify(s: str) -> str:
    s = (s or "").lower().strip()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_-]+", "-", s)
    return s.strip("-")

def normalize(s: str) -> str:
    return (s or "").replace("\r\n", "\n").strip()

def ensure_dir(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

def load_prompts(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    if not isinstance(data, list):
        raise ValueError("data/prompts.yaml must be a list")
    ids = []
    for p in data:
        for k in ["id", "category", "title", "description", "prompt"]:
            if k not in p or not str(p[k]).strip():
                raise ValueError(f"Prompt missing required field: {k}")
        ids.append(p["id"])
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate prompt id found")
    return data

def render_prompt(p: dict) -> str:
    title = normalize(str(p["title"]))
    desc = normalize(str(p["description"]))
    prompt_text = normalize(str(p["prompt"]))
    out = []
    out.append(f"## {title}\n\n")
    out.append(f"{desc}\n\n")
    out.append("```text\n")
    out.append(prompt_text + "\n")
    out.append("```\n\n")
    out.append("---\n\n")
    return "".join(out)

def render_category_page(category: str, prompts: list) -> str:
    out = []
    out.append(f"# {category}\n\n")
    out.append("Find prompts based on your specific task.\n\n")
    out.append("## Index\n\n")
    if prompts:
        for p in prompts:
            out.append(f"- [{normalize(p['title'])}](#{slugify(p['title'])})\n")
    else:
        out.append("- (No prompts yet)\n")
    out.append("\n---\n\n")
    for p in prompts:
        out.append(render_prompt(p))
    return "".join(out)

def write_category_pages(prompts: list):
    by_cat = defaultdict(list)
    unknown = []
    for p in prompts:
        cat = p["category"]
        if cat not in CATEGORY_TO_PATH:
            unknown.append(cat)
            continue
        by_cat[cat].append(p)

    for cat, path in CATEGORY_TO_PATH.items():
        ensure_dir(path)
        items = sorted(by_cat.get(cat, []), key=lambda x: normalize(x["title"]).lower())
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_category_page(cat, items))

    if unknown:
        unknown_unique = sorted(set(unknown))
        raise ValueError("Unknown categories in prompts.yaml: " + ", ".join(unknown_unique))

def write_master_page(prompts: list):
    by_cat = defaultdict(list)
    for p in prompts:
        by_cat[p["category"]].append(p)

    out = []
    out.append("# PROMPTS\n\n")
    out.append("This file is generated from `data/prompts.yaml`.\n\n")

    out.append("## Index\n\n")
    for cat in NAVIGATION_ORDER:
        if cat not in CATEGORY_TO_PATH:
            continue
        path = CATEGORY_TO_PATH[cat]
        out.append(f"- <!--citation:1-->\n")
    out.append("\n---\n\n")

    for cat in NAVIGATION_ORDER:
        if cat not in CATEGORY_TO_PATH:
            continue
        out.append(f"## {cat}\n\n")
        items = sorted(by_cat.get(cat, []), key=lambda x: normalize(x["title"]).lower())
        if not items:
            out.append("- (No prompts yet)\n\n")
            continue
        for p in items:
            out.append(f"- **{normalize(p['title'])}** — {normalize(p['description'])}\n")
        out.append("\n")

    with open("PROMPTS.md", "w", encoding="utf-8") as f:
        f.write("".join(out))

def main():
    prompts = load_prompts("data/prompts.yaml")
    write_category_pages(prompts)
    write_master_page(prompts)

if __name__ == "__main__":
    main()
