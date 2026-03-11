from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# In-memory storage for logs, used to temporarily store logs for get and post requests
logs : list[dict] = []

#create a pydantic model for the log entry, which will be used to validate the incoming data for the POST request
class LogCreate(BaseModel):
    level: str
    message: str

# Define a health check endpoint to verify that the API is running
@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

# Define an endpoint to create a log entry, which accepts a POST request with a JSON payload that matches the LogCreate model. 
# The log entry is stored in the in-memory logs list and a response is returned confirming that the log has been stored.
@app.post("/logs")
def create_log(payload: LogCreate) -> dict:
    item = payload.model_dump()
    logs.append(item)
    return {
        "message" : "log stored",
        "data" : item,
    }

# Define an endpoint to retrieve all log entries, which accepts a GET request and returns the list of logs stored in memory.
@app.get("/logs")
def get_logs() -> list[dict]:
    return logs