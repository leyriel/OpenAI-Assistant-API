from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os
load_dotenv()


USERNAME = os.environ.get("DB_USERNAME")
PASSWORD = os.environ.get('DB_PASSWORD')
SERVER = os.environ.get('DB_SERVER')
PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
