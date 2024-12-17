import os
from dotenv import load_dotenv

# class Config:
#     def __init__(self, env_file=".env"):
#         load_dotenv()
#         dsn = os.getenv("DSN")
#         access_token = os.getenv("ACCESS_TOKEN")
#         secret_access_key = os.getenv("SECRET_ACCESS_KEY")
#         s3_api_url = os.getenv("S3_API_URL")
#         bucket_name = os.getenv("BUCKET_NAME")

class Config:
    def __init__(self, env_file=".env"):
        load_dotenv()
        self.dsn = os.getenv("DSN")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.secret_access_key = os.getenv("SECRET_ACCESS_KEY")
        self.s3_api_url = os.getenv("S3_API_URL")
        self.bucket_name = os.getenv("BUCKET_NAME")