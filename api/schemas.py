from pydantic import BaseModel, Field

# Pydantic model for log entry validation
class LogCreate(BaseModel):
    level: str = Field(..., min_length=1, max_length=30, description="The severity level of the log entry")
    message: str = Field(..., min_length=1, max_length=200, description="The message for the log entry (max 200 characters)")