from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mariscos-secret"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
