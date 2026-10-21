from config import DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(DATABASE_URL)
session_maker = async_sessionmaker
