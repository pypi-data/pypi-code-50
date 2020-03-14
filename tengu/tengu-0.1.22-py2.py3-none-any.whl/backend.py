"""
FastAPI quickstart
"""

import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Local": socket.gethostbyname(socket.gethostname())}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
