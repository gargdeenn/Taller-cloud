from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_path = Column(String(200), unique=True, index=True)

