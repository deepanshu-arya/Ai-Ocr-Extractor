from sqlalchemy import Column, Integer, String
from .database import Base

class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    vendor = Column(String)
    total = Column(String)
    date = Column(String)