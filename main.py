from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/fullname/{name}:{family}")
async def say_fullname(name:str,family:str):
    return {"message": f"WE ARE VERY HAPPY FOR YOUR SIGN IN {name} {family}"}

