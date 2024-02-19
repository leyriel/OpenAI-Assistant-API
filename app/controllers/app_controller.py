from app.models.thread import Thread
from app.schemas.message import MessageModel
from app.schemas.thread import Thread
from app.schemas.create_chat import ChatCreateRequest
from app.repository.thread_repository import ThreadRepository
from app.schemas.continue_chat import ContinueChat
from app.services.openai import create_thread_and_run, submit_message
from app.services.openai import wait_on_run
from app.services.openai import get_messages
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

MATH_ASSISTANT_ID = os.environ.get("OPENAI_ASSISTANT_ID")


def get_chat_messages(db, data: Thread):
    thread_messages = get_messages(data)
    thread_messages_json = [MessageModel(role=m.role, text=m.content[0].text.value) for m in thread_messages]

    return thread_messages_json


def continue_chat(db, data: ContinueChat):
    thread = Thread(identifier=data.thread, id=data.thread)
    run = submit_message(MATH_ASSISTANT_ID, thread, data.message)
    run = wait_on_run(run, thread)
    thread_messages = get_messages(thread)

    thread_messages_json = [MessageModel(role=m.role, text=m.content[0].text.value) for m in thread_messages]

    return thread_messages_json


def create_chat(db, data: ChatCreateRequest):
    thread, run = create_thread_and_run(data.message)
    run = wait_on_run(run, thread)
    thread_messages = get_messages(thread)
    thread_messages_json = [MessageModel(role=m.role, text=m.content[0].text.value) for m in thread_messages]

    return thread_messages_json
