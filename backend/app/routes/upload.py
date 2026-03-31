from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import extract_text
from app.services.ai_parser import parse_with_ai
from app.services.pdf_service import extract_pdf

import os

router = APIRouter()

# create uploads folder if not exists
os.makedirs("uploads", exist_ok=True)

@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    path = f"uploads/{file.filename}"

    # Save file
    with open(path, "wb") as f:
        f.write(await file.read())

    # Check file type
    if file.filename.endswith(".pdf"):
        text = extract_pdf(path)
    else:
        text = extract_text(path)

    # AI parsing
    data = parse_with_ai(text)

    return {
        "filename": file.filename,
        "extracted_text": text,
        "structured_data": data
    }