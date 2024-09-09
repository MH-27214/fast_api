from fastapi import FastAPI

app = FastAPI()
static = "my API"


@app.post("/add")
async def add(text:str):
    global static
    static = text
    return {"message":"text added"}