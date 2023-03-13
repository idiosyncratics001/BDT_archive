from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dtServer.dtMeta import dtMeta as tags

app = FastAPI(
	openapi_tags=tags,
	title="Ryu's Data Tools",
    description="An collection of the best practices of engineering and data science as collected by Ryu.",
    version="0.0.1"
)

app.mount("/static", StaticFiles(directory="dtServer/static"), name="static")

from dtServer import dtRouter

app.include_router(dtRouter.dtRouter)