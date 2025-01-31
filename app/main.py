from fastapi import FastAPI
from app.api import router as api_router
from .utils.logger import setup_logging

app = FastAPI()
app.include_router(api_router)

setup_logging()

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}