from pydantic import BaseModel


class ChatCreateRequest(BaseModel):
    message: str
