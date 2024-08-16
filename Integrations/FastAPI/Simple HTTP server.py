from typing import Union

from fastapi import FastAPI

app = FastAPI()

try:
    print("")
except Exception as e:
    print(e)
finally:



@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None, t: Union[str, None] = None):
    return {"item_id": item_id, "q": q, "t": t}