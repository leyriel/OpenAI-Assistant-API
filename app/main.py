from fastapi import FastAPI
from app.config.db import Base, engine
from app.routes.chat_route import router as chat_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(chat_router, prefix="/chat")
