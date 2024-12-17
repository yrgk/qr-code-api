from pydantic import BaseModel

class QrCode(BaseModel):
    url: str