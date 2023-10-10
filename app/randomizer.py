from fastapi import FastAPI
from random import randint

app = FastAPI()

@app.get("/percentage")
async def get_random_percentage():
    return {'percentage': randint(0, 100)}

@app.get("/limits")
async def get_random_percentage_with_limits(lower_limit: int, upper_limit: int):
    return {'percentage': randint(lower_limit, upper_limit)}
