from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {
        "total_receipts": 120,
        "total_spent": 50000,
        "top_vendor": "Reliance"
    }