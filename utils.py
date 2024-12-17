import qrcode
import boto3
from io import BytesIO

from config import Config

def generate_and_upload_qr(link: str, object_name: str) -> str:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    config = Config()

    session = boto3.session.Session()
    s3 = session.client(
        service_name="s3",
        endpoint_url=config.s3_api_url,
        aws_access_key_id=config.access_token,
        aws_secret_access_key=config.secret_access_key,
    )
    s3.upload_fileobj(buffer, config.bucket_name, object_name, ExtraArgs={"ContentType": "image/png"})

    # Формирование публичной ссылки
    return f"{config.s3_api_url}/{config.bucket_name}/{object_name}"