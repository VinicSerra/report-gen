from fastapi import Depends
from typing_extensions  import Any, Annotated
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
 
import src.consts as consts
connection_string = (
    "mssql+pyodbc://sgrrmuser:#BJ_live2021@10.221.121.240/SGRRM?driver=ODBC+Driver+17+for+SQL+Server"
    
)
engine: Engine = create_engine(connection_string)
session: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Model: Any = declarative_base()
 
def get_db() -> Session:
    db = session()
    try:
        yield db
    finally:
        db.close()
 
Database = Annotated[Session, Depends(get_db)]