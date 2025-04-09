from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from modules import profile, resume

app = FastAPI()

app.include_router(profile.router)
app.include_router(resume.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}