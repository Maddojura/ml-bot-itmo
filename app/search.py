#import aiohttp
#import feedparser
#import requests
#from app.config import config
#import xml.etree.ElementTree as ET
#from app.utils.logger import get_logger



#async def search_web(query, num_results=3):
    #logger = await get_logger()
    #url = "https://yandex.com/search/xml"
    #params = {
        #"user": config.SEARCH_FOLDER_ID,
        #"key": config.SEARCH_API_KEY,
        #"query": query,
        #}
    #xml_data = """<?xml version="1.0" encoding="utf-8"?>
    #<request>
       #<query>yandex</query>
       # <sortby order="descending">tm</sortby>
        #<groupings>
           # <groupby attr="" mode="flat" groups-on-page="10" docs-in-group="1" />
           # </groupings>
        #<maxpassages>4</maxpassages>
    #</request>
        #"""
    
# Параметры API-авторизации (они всё равно передаются в URL)
   # params = {
        #"user": config.SEARCH_FOLDER_ID,
        #"key": config.SEARCH_API_KEY,
    #}

    # Отправляем POST-запрос
    #response = requests.post(url, params=params, data=xml_data)
    #logger.info(response.text)
   # try:
        #response = requests.get(url, params=params)
        #response.raise_for_status()
        #data = response.json()
        #logger.info(data)
        # Извлекаем нужную информацию
       # return [
            #{
                #"title": item.get("title"),
                #"url": item.get("url"),
                #"snippet": item.get("snippet")
           # }
           # for item in data.get("results", [])
       # ]

    #except requests.exceptions.RequestException as e:
        #print(f"Ошибка запроса: {e}")
   # except Exception as e:
        #print(f"Неизвестная ошибка: {e}")
#import requests
