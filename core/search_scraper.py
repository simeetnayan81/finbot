# core/search_scraper.py

from duckduckgo_search import DDGS
from newspaper import Article
from config import SEARCH_SITES
import time

def search_news(query, max_results=5):
    ddgs = DDGS()
    results = []
    for site in SEARCH_SITES:
        q = f"{query} {site}"
        search_results = ddgs.text(q, max_results=max_results)
        results.extend(search_results)
        time.sleep(1)
    return results[:max_results]

def scrape_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return {
            "title": article.title,
            "text": article.text,
            "url": url
        }
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return None
