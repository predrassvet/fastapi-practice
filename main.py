from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message() -> dict:
    mess = {"massage" : "привет"}
    return mess

