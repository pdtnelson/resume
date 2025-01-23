from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from modules import profile


app = FastAPI()

app.include_router(profile.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}