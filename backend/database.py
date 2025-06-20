from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

MARIADB_USER = os.getenv("MARIADB_USER", "root")
MARIADB_PASSWORD = os.getenv("MARIADB_PASSWORD", "")
MARIADB_HOST = os.getenv("MARIADB_HOST", "localhost")
MARIADB_DB = os.getenv("MARIADB_DB", "mariscos_db")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MARIADB_USER}:{MARIADB_PASSWORD}@{MARIADB_HOST}/{MARIADB_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

