import re
import json
from app.gpt_client import get_gpt_response
from app.search import search_web, get_news
from app.vector_db import VectorDB
from app.config import config
from .utils.logger import setup_logging

vector_db = VectorDB()

async def process_query(query: str, query_id: int) -> dict:
    try:
        question, options = extract_question_data(query)
        local_knowledge = await vector_db.search(question, top_k=3)
        web_results = await search_web(question)
        news_results = await get_news()

        context = "\n".join([
            "Локальные знания:",
            *[f"- {text}" for _, text in local_knowledge],
            "Веб-результаты:",
            *[f"- {url}" for url in web_results],
            "Новости:",
            *[f"- {url}" for url in news_results]
        ])

        gpt_response = await get_gpt_response(question, options, context)
        return {
            "id": query_id,
            "answer": gpt_response.get("answer"),
            "reasoning": f"{gpt_response['reasoning']} | Модель: {config.MODEL_NAME}",
            "sources": list(set(web_results + news_results))[:3]
        }
    except Exception as e:
        logger.error(f"Error in process_query: {str(e)}")
        raise