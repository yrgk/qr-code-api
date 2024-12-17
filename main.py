from fastapi import FastAPI

import time

import utils
import config
from models import QrCode

app = FastAPI()

@app.post("/create")
def create_qr_code(url: str, object_name: str):
    qr_code = utils.generate_and_upload_qr(url, object_name)

    return qr_code


@app.get("/qr")
def get_qr_code():
    """
        get qr code url by event_id and user_id
        return it
    """