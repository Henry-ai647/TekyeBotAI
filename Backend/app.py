from fastapi import FastAPI

app = FastAPI(
    title="TekyeBot AI",
    description="AI-powered multilingual restaurant assistant",
    version="1.0.0"
)

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
        "database": "Not Connected Yet",
        "ai": "Gemma (Coming Soon)"
    }
