from modules import profile
from fastapi import FastAPI

app = FastAPI()

app.include_router(profile.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}