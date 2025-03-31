from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(self):
        self.connection_string = os.getenv("MONGO_DB_URI")
        self.db_name = os.getenv("DB_NAME", "style_me")

config = Config()
