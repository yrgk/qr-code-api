from pydantic import BaseModel

class QrCode(BaseModel):
    url: str
    object_name: str