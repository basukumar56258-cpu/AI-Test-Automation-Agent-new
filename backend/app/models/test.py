from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from ..db import Base

class TestProject(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    requirement = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class TestCase(Base):
    __tablename__ = "test_cases"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, nullable=False)
    title = Column(String(200), nullable=False)
    steps = Column(Text, nullable=False)
    expected = Column(Text, nullable=False)
    status = Column(String(30), default="generated")
