import os

from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from src.routes.all_routes import router as all_routes

app = FastAPI(
    title=os.getenv("TITLE") if os.getenv("TITLE") else "tagsmart API V3",
    # root_path=os.getenv("ROOT_PATH") if os.getenv("ROOT_PATH") else "/",
    # docs_url=None

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(all_routes)

if __name__ == '__main__':
    logger.info("Started main")

    run("main:app", host="0.0.0.0", port=int(os.getenv("PORT")) if os.getenv("PORT") else 5017, reload=True)
