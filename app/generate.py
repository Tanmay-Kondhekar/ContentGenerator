from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.helpers import crud, utils, database, schemas, models
from starlette.concurrency import run_in_threadpool
from app.helpers.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def generate(payload: schemas.GeneratePayload, db: Session = Depends(get_db)):
    generted_text = await run_in_threadpool(utils.generate_content, db, payload.topic)
    return {"generated_text": generted_text}