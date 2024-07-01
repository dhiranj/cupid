from fastapi import HTTPException, Path
from starlette.status import HTTP_400_BAD_REQUEST

def validate_username(username: str = Path(..., max_length=50)):
    if len(username) > 50:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Username must be less than 50 characters")
    return username.lower()
