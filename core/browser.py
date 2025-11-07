import requests
from bs4 import BeautifulSoup

class Browser:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, path=""):
        response = requests.get(self.base_url + path)
        response.raise_for_status()
        return response.text

    def get_soup(self, html_content):
        return BeautifulSoup(html_content, "html.parser")
