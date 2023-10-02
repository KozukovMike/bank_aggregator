import os
from dotenv import load_dotenv


load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
USER='postgres'
PASSWORD='fantasy27'
HOST='localhost'
PORT='5432'
DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}'
