from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"hello fastAPI"}

@app.get("/world")
def world():
    return {"fastAPI world"}