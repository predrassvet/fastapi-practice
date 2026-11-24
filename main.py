from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message() -> dict:
    mess = {"message" : "привет"}
    return mess

@app.get("/hello/{name}")
def hello(name: str) -> dict:
    answer = {"hello" : f"hello {name}"}
    return answer

@app.get("/square/{number}")
def square(number: int) -> int:
    return number * number 