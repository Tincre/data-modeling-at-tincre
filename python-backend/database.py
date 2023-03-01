from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.environ.get(
    "DATABASE_URL"
)  # "postgresql://<pguser>:<password>@<host>:<port>/<pg-database-name>"
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError(f"SQLALCHEMY_DATABASE_URL is not set.")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # echo=True, uncomment to see lots of logs for sqlalchemy
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
