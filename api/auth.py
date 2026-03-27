from fastapi import Header, HTTPException

# Demo API key used by protected endpoints.
API_KEY = "mysecretkey"

# FastAPI dependency that rejects requests with a missing or invalid key.
def verify_api_key(x_api_key: str = Header(...)) -> None:
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid Key")
