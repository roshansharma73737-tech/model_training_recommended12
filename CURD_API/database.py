from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
import os
from dotenv import load_dotenv


# -- load_dotenv 
load_dotenv()

DB_Users = os.getenv("DB_users")
DB_Name = os.getenv("DB_name")
DB_Host = os.getenv("DB_host")
DB_POrt = os.getenv("DB_port ")
DB_passworD = os.getenv("DB_password")


# for only genral prin the  url ( not mandatory )
database_URL =  f"mysql+pymysql://{DB_Users}:{DB_passworD}:{DB_Host}:{DB_POrt}/{DB_Name}"


# create the engine  for the connection ----

engine = create_engine( database_URL,  pool_pre_ping=True, pool_recycle=3600, echo=False)
sessionLocal =  sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()

#  create the function  for the check the request of the connection or not -->

def get_connection():
    db =sessionLocal()
    try:
        yield db
    finally:
        db.close()