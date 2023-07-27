from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root()-> str:
    return "Fast api is up and running. Use swagger UI at /docs."


@app.post("/model/dollyv2/instruct_generate")
async def test():
    return {"post": "output"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)