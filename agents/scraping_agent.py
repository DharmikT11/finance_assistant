# agents/scraping_agent.py

import feedparser

class ScrapingAgent:
    def __init__(self):
        self.tech_companies = ["TCS", "INFOSYS", "WIPRO", "HCLTECH"]
        self.base_rss_url = "https://news.google.com/rss/search?q={company}+earnings+india"

    def get_earnings_news(self):
        all_news = []

        for company in self.tech_companies:
            rss_url = self.base_rss_url.format(company=company)
            feed = feedparser.parse(rss_url)

            for entry in feed.entries:
                all_news.append({
                    "company": company,
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.published
                })
        return all_news

# Test
if __name__ == "__main__":
    agent = ScrapingAgent()
    news = agent.get_earnings_news()
    print("📰 Recent Earnings News:")
    if news:
        for n in news:
            print(f"- {n['company']}: {n['title']} ({n['published']})")
    else:
        print("No relevant news found. Try again later.")
