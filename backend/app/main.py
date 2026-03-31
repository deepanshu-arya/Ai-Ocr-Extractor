from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload import router  # your upload route

# ✅ FIRST create app
app = FastAPI()

# ✅ THEN add CORS (AFTER app is created)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ include routes
app.include_router(router)

# optional test route
@app.get("/")
def home():
    return {"message": "Backend is running"}