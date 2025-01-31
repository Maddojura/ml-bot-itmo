import asyncio
import uvloop
from fastapi import FastAPI
from app.api import router as api_router
from app.utils.logger import get_logger

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = FastAPI()
app.include_router(api_router)



@app.get("/healthcheck")
async def healthcheck():
    logger = await get_logger()
    return {"status": "ok"}
    