from fastapi import FastAPI
import uvicorn
from scripts.core.services.service import app as apple

app_main = FastAPI()

app_main.include_router(apple)


if __name__ == "__main__":
    uvicorn.run("new:app_main")
