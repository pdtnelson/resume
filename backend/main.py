import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from modules import profile, resume, auth

app = FastAPI()

app.include_router(profile.router)
app.include_router(resume.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"app_status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
