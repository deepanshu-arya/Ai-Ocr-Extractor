from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

from app.services.export_service import export_excel, export_json

router = APIRouter()

# ✅ Define proper request body
class ExportRequest(BaseModel):
    data: List[Dict]

@router.post("/export")
def export(request: ExportRequest):
    data = request.data

    export_excel(data, "exports/data.xlsx")
    export_json(data, "exports/data.json")

    return {
        "message": "Export successful",
        "records": len(data)
    }