from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from config import settings

Base = declarative_base()
async_engine = create_async_engine(url=settings.DATABASE_URL)
async_session_factory = async_sessionmaker(bind=async_engine, autoflush=False)
