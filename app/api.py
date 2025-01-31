from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.processing import process_query
from app.utils.logger import get_logger
from fastapi.security import OAuth2PasswordBearer
from app.utils.logger import get_logger

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth")

class QueryRequest(BaseModel):
    query: str
    id: int

class QueryResponse(BaseModel):
    id: int
    answer: int | None
    reasoning: str
    sources: str

@router.post("/api/request")
async def handle_request(request: QueryRequest) -> QueryResponse:
    logger = await get_logger()
    try:
        response_data = await process_query(request.query, request.id)
        return QueryResponse(**response_data)
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/api/auth")
async def auth():
    return {"token": "fake-token"}

@router.post("/api/preprocess")
async def preprocess(text: str):
    return {"processed_text": text.lower().strip()}