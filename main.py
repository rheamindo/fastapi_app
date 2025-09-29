from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env, if any

app = FastAPI()

@app.get("/")
async def root():
    message = os.getenv("WELCOME_MESSAGE", "Hello World")
    return {"message": message}
