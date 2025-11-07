import re

class Parser:
    def __init__(self, data):
        self.data = data

    def clean_quotes(self):
        cleaned = []
        for item in self.data:
            text = re.sub(r"[^a-zA-Z0-9\s\.,!?\-']", "", item["text"])
            cleaned.append({
                "text": text.strip(),
                "author": item["author"].title(),
                "tags": [t.lower() for t in item["tags"]]
            })
        return cleaned
