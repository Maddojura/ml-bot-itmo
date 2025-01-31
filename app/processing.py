import re
import json
from app.gpt_client import get_gpt_response
#from app.search import search_web #, get_news
from app.vector_db import VectorDB
from app.config import config
from app.utils.logger import get_logger

vector_db = VectorDB()

def extract_question_data(input_string: str):
    # Ensure there is at least one "?" in the string
    if "?" not in input_string:
        raise ValueError("Input must contain a question mark (?)")

    # Split the string at the first occurrence of "?"
    question_part, _, options_part = input_string.partition("?")

    # Trim whitespace and format the query
    query = question_part.strip() + "?"

    # Split options by newline and remove empty entries
    options = [option.strip() for option in options_part.split("\n") if option.strip()]

    return query, options

async def process_query(query: str, query_id: int) -> dict:
    logger = await get_logger()
    try:
        logger.info("test1")
        question, options = extract_question_data(query)
        #local_knowledge = await vector_db.search(question, top_k=3)
        #web_results = await search_web(question)
        #news_results = get_news()


        #context = "\n".join([
            #"Локальные знания:",
            #*[f"- {text}" for _, text in local_knowledge],
            #"Веб-результаты:",
            #*[f"- {url}" for url in web_results],
            #"Новости:",
            #*[f"- {url}" for url in news_results]
        #])
        logger.info("test2")
        gpt_response = await get_gpt_response(question, options)
        logger.info("test3")
        logger.info(gpt_response)
        return {
            "id": query_id,
            "answer": gpt_response.get("answer"),
            "reasoning": f"{gpt_response['reasoning']} ",
            "sources": f"Модель: {config.MODEL_NAME}"
        }
    except Exception as e:
        await logger.error(f"Error in process_query: {str(e)}")
        raise