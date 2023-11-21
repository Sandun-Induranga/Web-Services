from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: Union[int, str]):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app)
