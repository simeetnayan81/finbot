# 📈 Finbot - Finance News Aggregator using Agentic AI (Gemini + AutoGen)

An Agentic AI-powered system that automatically **searches, scrapes, and summarizes** financial news about a given stock or security from trusted websites like **Yahoo Finance**, **Bloomberg**, **Reuters**, and more. This project leverages **Google's Gemini 2.0 Flash model** for summarization and **AutoGen** for multi-agent orchestration.

---

## ✨ Features

- 🔍 **Search** recent articles related to a stock symbol (e.g., `TSLA`, `AAPL`).
- 📰 **Scrape** full articles from reliable news sources.
- 🧠 **Summarize** each article using Gemini 2.0 Flash into concise bullet points.
- 🤖 Built using agentic workflows powered by **AutoGen**.
- 🌐 Easily extendable to new sources or agents.

---

## 🧠 Tech Stack

| Tool | Purpose |
|------|---------|
| 🧠 Gemini 2.0 Flash | Large Language Model for summarization |
| 🤖 AutoGen | Multi-agent orchestration and task automation |
| 🔎 duckduckgo-search | Web search for news articles |
| 📰 newspaper3k | Article extraction and content scraping |
| 🐍 Python | Core scripting language |
| 🧰 lxml, BeautifulSoup | HTML parsing and cleaning |

---

## 📦 Installation

1. **Clone the repo**:
    ```bash
    git clone git@github.com:simeetnayan81/finbot.git
    cd finbot
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv .finbot
    source .finbot/bin/activate  # or .\.finbot\Scripts\activate on Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install additional compatibility packages** (if needed):
    ```bash
    pip install lxml-html-clean "lxml[html_clean]"
    ```

---

## 🔑 Environment Variables

Create a `.env` file with your API key:

```env
GEMINI_API_KEY=your_google_gemini_api_key
