import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
    GPT_API_KEY = os.getenv("GPT_API_KEY")
    NEWS_URL = "https://news.itmo.ru/ru/rss/"
    MODEL_NAME = "Yandex GPT"
    PARSED_SITES = [
        "https://itmo.ru",
        "https://abit.itmo.ru",
        "https://news.itmo.ru"
    ]
    
config = Config()