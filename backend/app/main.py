from fastapi import FastAPI

app = FastAPI(title="AI StudyMate API")


@app.get("/health")
def health_check():
    return {"status": "ok"}