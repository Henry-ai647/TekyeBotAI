from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="TekyeBot AI",
    description="AI-powered multilingual restaurant assistant",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "project": "TekyeBot AI",
        "status": "Running",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "server": "Online",
        "database": "Ready",
        "ai": "Coming Soon"
    }
