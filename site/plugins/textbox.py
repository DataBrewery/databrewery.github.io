from pelican import signals
from collections import defaultdict

def generate_textboxes(generator):
    # Collect boxes
    boxes = defaultdict(dict)
    for page in generator.hidden_pages:
        if "textbox" not in page.metadata:
            continue
        box = page.metadata["textbox"]
        boxes[page.metadata["slug"]][box] = page

    # Assign pages to boxes
    for page in generator.pages:
        if "slug" not in page.metadata:
            continue
        slug = page.metadata["slug"]
        page.metadata["textboxes"] = boxes.get(slug, {})

def register():
    signals.pages_generator_finalized.connect(generate_textboxes)

