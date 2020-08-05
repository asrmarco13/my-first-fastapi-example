from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.database import Base

SQLALCHEMY_DATABASE_URL = "postgresql://gisdb:gisdb@localhost:5432/gisdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
