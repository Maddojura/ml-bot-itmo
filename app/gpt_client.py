import aiohttp
import json
from app.config import config

async def get_gpt_response(question: str, options: dict, context: str) -> dict:
    prompt = f"""
    Ты эксперт по Университету ИТМО. Ответь на вопрос, используя контекст:
    {context}
    
    Вопрос: {question}
    {"Варианты ответов: " + ", ".join([f"{num}. {text}" for num, text in options.items()]) if options else ""}
    
    Формат ответа JSON:
    {{
        "answer": номер_правильного_варианта || null,
        "reasoning": "Обоснование ответа на русском языке"
    }}
    """
    
    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Api-Key {config.GPT_API_KEY}",
                "Content-Type": "application/json"
            }
            async with session.post(
                "https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                headers=headers,
                json={
                    "modelUri": "gpt://<your-folder-id>/yandexgpt-lite",
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
                return json.loads(result['result']['alternatives'][0]['message']['text'])
    except Exception as e:
        return {"answer": None, "reasoning": "Ошибка при обработке запроса"}