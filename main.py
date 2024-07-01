from typing import Union

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/healthycheck")
def read_root():
    return {"Hello": "World"}


@app.post("/remove-bg")
def remove_bg(req: Request):
    try:
      print(x)
    except:
      print('An exception occurred')