from fastapi import FastAPI

from app.model import Model

app = FastAPI()
model = Model()


@app.get("/")
def index():
    return {"Status": "Online"}


@app.post("/generate")
def generate(context: str, max_length: int = 100):
    context, horoscope = model.predict(context, max_length=max_length)

    return {
        "context": context,
        "horoscope": horoscope,
    }
