from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import psycopg2 # type: ignore
import time
from .config import settings

# FORMAT: postgresql://<username>:<password>@<ip-address/hostname>/<database_name>
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}\
@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass

# while True:

#     try:
#         conn = psycopg2.connect(
#         dbname="fastapi", 
#         user="postgres", 
#         password="password123", 
#         host="localhost", 
#         port=5432
#         )
#         cur = conn.cursor()
#         print("Database connection successful")
#         break
                
#     except Exception as e:
#         print("Connecting to database failed")
#         print("Error: ", e)
#         time.sleep(2)

