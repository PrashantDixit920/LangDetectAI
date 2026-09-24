from pydantic import BaseModel, Field, field_validator


class PredictionRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Text whose language needs to be identified"
    )
    
    @field_validator("text")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("Text cannot contain only whitespace.")

        return value    


class PredictionResponse(BaseModel):
    language: str
    confidence: float