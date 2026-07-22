from fastapi import FastAPI
from backend.routers.auth import router

app = FastAPI()

app.include_router(router, prefix="/auth", tags=["auth"])


@app.get("/")
def root():
    return {"message": "API работает"}
