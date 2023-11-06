import os
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
# import redis

# r = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379, db=int(os.getenv("REDIS_DB") if os.getenv("REDIS_DB") is not None else 0))
cdb = None
DBSession: sessionmaker = None
Base = None


class Settings:
    PROJECT_NAME: str = "tagsmart"
    EPC_STATUS: str = os.getenv("EPC_STATUS")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = int(os.getenv("POSTGRES_PORT", 5432))  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
logger.info(settings.DATABASE_URL)
logger.debug(f"postgresql+psycopg2://{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}")
engine = create_engine(settings.DATABASE_URL, connect_args={'connect_timeout': 2}, pool_size=0, max_overflow=-1,
                       pool_recycle=3600)

try:
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    logger.info("Database connected successfully")

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as err:
    logger.error("Database Connection Error - {}".format(err))


