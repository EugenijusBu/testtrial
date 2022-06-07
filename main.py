from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    sentence: str
    letters: str

@app.post("/modify")
def modify(item: Item):
    s = item.sentence.replace(item.letters,"")
    return s