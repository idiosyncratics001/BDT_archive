from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dtServer.dtMeta import tags_metadata as tags

app = FastAPI(openapi_tags=tags)

app.mount("/static", StaticFiles(directory="dtServer/static"), name="static")

from dtServer import dtRouter

app.include_router(dtRouter.dtRouter)