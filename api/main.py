import os
import secrets

from typing import Dict
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import (
        status,
        Depends,
        FastAPI,
        HTTPException
    )


app = FastAPI()
security = HTTPBasic()


def load_admin_credentials() -> Dict[str, bytes]:
    admin_credentials = {
            "username": bytes(os.getenv("ADMIN_USER"), "utf-8"),
            "password": bytes(os.getenv("ADMIN_PASS"), "utf-8")
        }

    return admin_credentials


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    current_password_bytes = credentials.password.encode("utf8")

    admin_credentials = load_admin_credentials()

    is_correct_username = secrets.compare_digest(
            current_username_bytes,
            admin_credentials["username"]
        )
    is_correct_password = secrets.compare_digest(
            current_password_bytes,
            admin_credentials["password"]
        )

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha estão incorretos",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/")
def main_route(username: str = Depends(get_current_username)):
    return {"message": "Olá candidato, seja bem vindo ao Vars!", "username": username}