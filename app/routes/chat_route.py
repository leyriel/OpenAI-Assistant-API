from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.config.db import SessionLocal
from app.controllers.app_controller import read_example, continue_chat, get_chat_messages
from app.controllers.app_controller import create_chat
from app.schemas.thread import Thread
from app.schemas.create_chat import ChatCreateRequest
from app.schemas.continue_chat import ContinueChat

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/example/{example_id}")
def example_route(example_id: int, db: Session = Depends(get_db)):
    return read_example(db, example_id)


@router.get("/{thread_id}")
def get_chat_route(thread_id: str, db: Session = Depends(get_db)):
    data = Thread(id=thread_id)
    return get_chat_messages(db, data)


@router.post("/continue")
def create_chat_route(request_data: ContinueChat, db: Session = Depends(get_db)):
    return continue_chat(db, request_data)


@router.post("/create")
def create_chat_route(request_data: ChatCreateRequest, db: Session = Depends(get_db)):
    return create_chat(db, request_data)
