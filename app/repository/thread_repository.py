from sqlalchemy import String
from sqlalchemy.orm import Session
from app.config.db import SessionLocal
from app.models.thread import Thread


class ThreadRepository:
    def __init__(self):
        self.db_session = SessionLocal()

    def get_thread_by_id(self, thread_id: int) -> Thread:
        return self.db_session.query(Thread).filter(Thread.id == thread_id).first()

    def create_thread(self, identifier: String) -> Thread:
        new_thread = Thread(identifier=identifier)
        self.db_session.add(new_thread)
        self.db_session.commit()
        self.db_session.refresh(new_thread)
        return new_thread

    def update_thread(self, thread_id: int, identifier: String) -> Thread:
        thread = self.db_session.query(Thread).filter(Thread.id == thread_id).first()
        if thread:
            thread.identifier = identifier
            self.db_session.commit()
            self.db_session.refresh(thread)
        return thread

    def delete_thread(self, thread_id: int) -> None:
        thread = self.db_session.query(Thread).filter(Thread.id == thread_id).first()
        if thread:
            self.db_session.delete(thread)
            self.db_session.commit()

    def list_threads(self) -> list[Thread]:
        return self.db_session.query(Thread).all()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db_session.close()
