import aiohttp
import json
from app.config import config
from app.utils.logger import get_logger

async def get_gpt_response(question: str, options: list) -> dict:
    logger = await get_logger()
    prompt = f"""
    Ты эксперт по Университету ИТМО. Ответь на вопрос 
    Вопрос: {question}
    {"Варианты ответов: " + ", ".join(options) +  ""}
    
    Формат ответа JSON, не нужно добавлять спецсимволы в текст ответа, например `:
    {{
        "answer": номер_правильного_варианта || null,
        "reasoning": "Обоснование ответа на русском языке"
    }}
    """
    
    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {config.GPT_API_KEY}",
            }
            logger.info(headers)
            async with session.post(
                "https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                headers=headers,
                json={
                    "modelUri": "gpt://b1gnc9ajvqneho8vt7ba/yandexgpt-lite",
                    "completionOptions": {
                        "stream": False,
                        "temperature": 0.1,
                        "maxTokens": 1000
                    },
                    "messages": [{
                        "role": "user",
                        "text": prompt
                    }]
                }
            ) as response:
                result = await response.json()
                json_response = result['result']['alternatives'][0]['message']['text']
                json_response = json_response.replace("`", "")
                return json.loads(json_response)
    except Exception as e:
        return {"answer": None, "reasoning": "Ошибка при обработке запроса"}