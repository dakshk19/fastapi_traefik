from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read():
    return {"msg": "Hello Fastapi with traefik"}