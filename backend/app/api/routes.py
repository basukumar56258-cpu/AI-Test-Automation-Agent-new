from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from ..agents.test_agent import TestAutomationAgent
from ..services.runner import run_smoke_test

router = APIRouter(prefix="/api")
agent = TestAutomationAgent()

class GenerateRequest(BaseModel):
    requirement: str

class RunRequest(BaseModel):
    url: HttpUrl

@router.get("/health")
def health():
    return {"status":"ok","service":"TestPilot AI"}

@router.post("/test-cases/generate")
def generate(req: GenerateRequest):
    if not req.requirement.strip():
        raise HTTPException(400, "Requirement is required")
    return {"test_cases": agent.generate(req.requirement)}

@router.post("/tests/run")
def run_test(req: RunRequest):
    return run_smoke_test(str(req.url))
