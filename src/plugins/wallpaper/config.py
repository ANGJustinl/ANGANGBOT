from typing import Optional
from pydantic import BaseModel, field_validator

class Config(BaseModel):
    daily_news_api_key: Optional[str] = None

    @field_validator("daily_news_api_key")
    @classmethod
    def check_daliy_news_api_key(cls, v: str) -> str:
        if v:
            return v
        raise ValueError("daily_news_api_key must not be empty")