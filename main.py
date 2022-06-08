from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



@app.get("/get-modified")
def modify(sentence: str,letter: str):

    s = sentence.replace(letter,"")
    return {"modified-sentence" : s}