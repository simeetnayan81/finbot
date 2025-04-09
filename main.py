# main.py

from core.search_scraper import search_news, scrape_article
from agents.summarizer import summarize_articles

def main():
    ticker = input("Enter stock ticker (e.g., AAPL, TSLA): ").strip().upper()
    print(f"\n🔍 Searching news for {ticker}...\n")
    results = search_news(f"{ticker} stock news")

    articles = []
    for r in results:
        print(f"📰 {r['title']} - {r['href']}")
        article = scrape_article(r['href'])
        if article:
            articles.append(article)

    print("\n📚 Summarizing news articles...\n")
    summaries = summarize_articles(articles)

    print("\n✅ Final Summary:")
    for i, summary in enumerate(summaries, 1):
        print(f"\n--- Article {i} ---\n{summary}")

if __name__ == "__main__":
    main()
