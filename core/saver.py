import json
import logging

class Saver:
    def __init__(self, output_path):
        self.output_path = output_path

    def save(self, data):
        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info(f"Dados salvos em {self.output_path}")
