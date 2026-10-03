from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./testpilot.db"
    cors_origins: str = "http://localhost:5173"
    llm_api_key: str = ""
    llm_base_url: str = ""
    llm_model: str = ""

settings = Settings()
