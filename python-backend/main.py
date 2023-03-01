# https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_route():
    return {"message": "Hello, world!"}
