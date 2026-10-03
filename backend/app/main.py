from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .db import Base, engine
from .models.test import TestProject, TestCase
from .api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TestPilot AI API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[x.strip() for x in settings.cors_origins.split(",")],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)
app.include_router(router)

@app.get("/")
def root():
    return {"name":"TestPilot AI","docs":"/docs"}
