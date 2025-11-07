import json
import logging
from core.browser import Browser
from core.extractor import Extractor
from core.parser import Parser
from core.saver import Saver

import os

os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Configuração
with open("config/settings.json") as f:
    settings = json.load(f)

logging.basicConfig(
    filename=settings["log_path"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Iniciando Data Harvester...")

    browser = Browser(settings["target_url"])
    html = browser.fetch_page()
    soup = browser.get_soup(html)

    extractor = Extractor(soup)
    raw_data = extractor.extract_quotes()

    parser = Parser(raw_data)
    clean_data = parser.clean_quotes()

    saver = Saver(settings["output_path"])
    saver.save(clean_data)

    logging.info("Coleta e limpeza concluídas com sucesso.")

if __name__ == "__main__":
    main()
