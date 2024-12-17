from fastapi import FastAPI

import time

import utils
import config
from models import QrCode

app = FastAPI()

@app.post("/create")
def create_qr_code(body: QrCode):
    qr_code = utils.generate_and_upload_qr(body.url, body.object_name)

    return qr_code


@app.get("/qr")
def get_qr_code():
    """
        get qr code url by event_id and user_id
        return it
    """