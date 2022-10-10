import time
from typing import Dict

import jwt


from settings import JWT_ALGORITHM, JWT_SECRET

def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(username: str) -> Dict[str, str]:
    payload = {
        "username": username,
        "expires": time.time() + 600 #15 min
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def getUser(token: str) -> str:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token["username"]
    except:
        return ""