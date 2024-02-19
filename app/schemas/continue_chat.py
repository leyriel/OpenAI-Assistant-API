from pydantic import BaseModel


class ContinueChat(BaseModel):
    message: str
    thread: str
