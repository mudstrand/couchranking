import time
from typing import Dict

import jwt

JWT_SECRET = 'thesecretofgreenbush'
JWT_ALGORITHM = 'HS256'


# def token_response(token: str):
#     return {
#         "access_token": token
#     }
#
#
# def signJWT(email: str) -> Dict[str, str]:
#     payload = {
#         "email": email,
#         "expires": time.time() + 600
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
#
#     return token_response(token)

def sign_jwt(email: str):
    payload = {
        "email": email,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}