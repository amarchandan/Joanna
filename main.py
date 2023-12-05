import asyncio
import uvicorn
import os
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, StreamingResponse
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = os.getenv("PORT", 8080)
    uvicorn.run(app, host=HOST, port=PORT)
