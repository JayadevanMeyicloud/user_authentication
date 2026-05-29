from fastapi import Request, HTTPException, Depends
from jose import jwt, JWTError
from app.config import SECRET_KEY, ALGORITHM


def get_current_user(request: Request):

    auth = request.headers.get("Authorization")
    if not auth:
        raise HTTPException(status_code=401, detail="Token missing")
    try:
        token = auth.split(" ")[1]

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def require_admin(current_user: dict = Depends(get_current_user)):

    if current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Access denied")

    return current_user