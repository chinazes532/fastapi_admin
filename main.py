from fastapi import FastAPI

from contextlib import asynccontextmanager

from routes import router as text
from database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await create_tables()
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)
app.include_router(text)