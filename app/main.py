from fastapi import FastAPI
from pydantic import BaseModel

from app.analyzer import analyze_security_event

app = FastAPI()


class SecurityLog(BaseModel):
    log: str


@app.get("/")
async def root():
    return {"message": "AI SOC Copilot Running"}


@app.post("/analyze")
async def analyze(security_log: SecurityLog):

    result = analyze_security_event(security_log.log)

    return {
        "submitted_log": security_log.log,
        "analysis": result
    }