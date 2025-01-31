import aiohttp
import feedparser
from app.config import config

async def search_web(query: str) -> list:
    try:
        async with aiohttp.ClientSession() as session:
            params = {
                "key": config.SEARCH_API_KEY,
                "cx": config.SEARCH_ENGINE_ID,
                "q": f"{query} site:{config.PARSED_SITES[0]} OR site:{config.PARSED_SITES[1]} OR site:{config.PARSED_SITES[2]}",
                "num": 3
            }
            async with session.get("https://yandex.com/search/xml", params=params) as response:
                results = await response.json()
                return [item["link"] for item in results.get("items", [])][:3]
    except Exception:
        return []

async def get_news() -> list:
    try:
        feed = feedparser.parse(config.NEWS_URL)
        return [entry.link for entry in feed.entries[:3]]
    except Exception:
        return []