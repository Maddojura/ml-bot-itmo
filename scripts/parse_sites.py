import aiohttp
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
from app.config import config
import asyncio

async def parse_site(url: str) -> list:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                data = []
                for link in soup.find_all('a', href=True):
                    page_url = urljoin(url, link['href'])
                    if any(site in page_url for site in config.PARSED_SITES):
                        page_content = await parse_page(page_url)
                        data.append({
                            "url": page_url,
                            "text": page_content
                        })
                return data
    except Exception as e:
        print(f"Error parsing {url}: {str(e)}")
        return []

async def parse_page(url: str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                return ' '.join([p.get_text() for p in soup.find_all('p')])
    except Exception:
        return ""

async def main():
    all_data = []
    for site in config.PARSED_SITES:
        all_data.extend(await parse_site(site))
    with open('../data/parsed_data.json', 'w') as f:
        json.dump(all_data, f, ensure_ascii=False)

if __name__ == "__main__":
    asyncio.run(main())