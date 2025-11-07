class Extractor:
    def __init__(self, soup):
        self.soup = soup

    def extract_quotes(self):
        quotes = []
        for quote in self.soup.select(".quote"):
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.select(".tag")]
            quotes.append({
                "text": text,
                "author": author,
                "tags": tags
            })
        return quotes
