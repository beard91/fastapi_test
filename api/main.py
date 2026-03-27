from fastapi import FastAPI, HTTPException, Depends
from .schemas import LogCreate
from .auth import verify_api_key

# Application entry point for the logging API.
app = FastAPI()

# Accepted severity values for incoming log entries.
LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

# Temporary in-memory store; entries are lost when the process restarts.
logs : list[dict] = []

# Lightweight liveness check used by clients or deployment tooling.
@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

# Validates the payload, assigns a sequential ID, and stores the entry.
# Protected by API key authentication.
# Depends as a parameter to ensure the auth check runs before the endpoint logic.
@app.post("/logs")
def create_log(payload: LogCreate, _: None = Depends(verify_api_key)) -> dict:
    if payload.level not in LOG_LEVELS:
        raise HTTPException(status_code=400, detail="Invalid log level")
    item = {
        "id" : len(logs) + 1,
        "level" : payload.level,
        "message" : payload.message,
    }
    logs.append(item)

    return item

# Returns all currently stored log entries.
# Protected by API key authentication.
# Depends as a parameter to ensure the auth check runs before the endpoint logic.
@app.get("/logs")
def get_logs(_: None = Depends(verify_api_key)) -> list[dict]:
    return logs

# Looks up a single log entry by its numeric ID.
# Protected by API key authentication.
# Depends as a parameter to ensure the auth check runs before the endpoint logic.
@app.get("/logs/{log_id}")
def get_log(log_id: int, _: None = Depends(verify_api_key)) -> dict:
    for log in logs:
        if log["id"] == log_id:
            return log
    raise HTTPException(status_code=404, detail="Log not found")
