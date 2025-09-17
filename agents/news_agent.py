import feedparser
from newspaper import Article

class NewsAgent:
    def __init__(self):
        self.base_url = "https://news.google.com/rss/search?q={query}"

    def get_news(self, ticker, num_articles=5):
        url = self.base_url.format(query=ticker)
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries[:num_articles]:
            article_text = ""
            try:
                art = Article(entry.link)
                art.download()
                art.parse()
                article_text = art.text
            except Exception as e:
                article_text = ""
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": getattr(entry, "published", ""),
                "content": article_text
            })
        return articles
