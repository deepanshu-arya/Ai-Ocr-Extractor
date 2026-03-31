from pydantic import BaseModel

class ReceiptSchema(BaseModel):
    vendor: str
    total: str
    date: str