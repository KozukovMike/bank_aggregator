import os
from dotenv import load_dotenv


load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}'
