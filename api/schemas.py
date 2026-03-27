from pydantic import BaseModel

# Pydantic model for log entry validation
class LogCreate(BaseModel):
    level: str
    message: str