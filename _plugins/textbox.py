from pelican import signals
from collections import defaultdict

def generate_textboxes(generator):
    # Collect boxes
    boxes = defaultdict(dict)
    for page in generator.hidden_pages:
        if "textbox" not in page.metadata:
            continue

        if "column" in page.metadata:
            box = int(float(page.metadata["column"])) - 1
        else:
            box = 0

        row = int(float(page.metadata["row"]))
        parent = page.metadata["parent"]
        if row not in boxes[parent]:
            boxes[parent][row] = defaultdict(dict)
        boxes[parent][row][box] = {"content" : page.content, "metadata" : page.metadata}

    # Assign pages to boxes
    for page in generator.pages:
        if "slug" not in page.metadata:
            continue
        slug = page.metadata["slug"]
        textboxes = boxes.get(slug, {})
        page.metadata["textboxes"] = textboxes

def register():
    signals.page_generator_finalized.connect(generate_textboxes)

