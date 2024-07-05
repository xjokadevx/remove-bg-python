from typing import Union

from fastapi import FastAPI
from models.ImageRequest import ImageRequest

app = FastAPI()


@app.get("/healthycheck")
def read_root():
    return {"Hello": "World"}


@app.post("/remove-bg")
def remove_bg(imgRequest: ImageRequest):
    try:
      print(x)
    except:
      print('An exception occurred')
