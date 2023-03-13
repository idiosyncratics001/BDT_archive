#"last modified": "3-1-2021"
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import dtServer.dtMeta as dtMeta
import dtServer.dtMain as dtMain
import dtServer.dtAbout as dtAbout

templates = Jinja2Templates(directory="dtServer/templates")

dtRouter = APIRouter()

@dtRouter.get("/", tags=["root"])
async def root():
    return {"app": "Data Tools", "Author": "Rei Ryu"}
@dtRouter.get("/me", tags=["root"])
async def return_me():
    return dtMeta.return_me("root")

#<<>><<>><<>><<>><<>><<>><<>><<>>

@dtRouter.get("/main", response_class=HTMLResponse, tags=["main"])
async def main(request: Request):
    pageid = dtMain.pageid()
    return templates.TemplateResponse("dtMain.html", {"request": request ,"pageid": pageid})
@dtRouter.get("/main/me", tags=["main"])
async def return_me():
    return dtMeta.return_me("main")

#<<>><<>><<>><<>><<>><<>><<>><<>>

@dtRouter.get("/dashboard", tags=["dashboard"])
async def dashboard(request: Request):
    pageid = dtMain.pageid()
    return templates.TemplateResponse("dtDashboard.html", {"request": request ,"pageid": pageid})
@dtRouter.get("/dashboard/me", tags=["dashboard"])
async def return_me():
    return dtMeta.return_me("dashboard")

#<<>><<>><<>><<>><<>><<>><<>><<>>

@dtRouter.get("/about", response_class=HTMLResponse, tags=["about"])
async def about(request: Request):
    pageid = dtAbout.pageid()
    return templates.TemplateResponse("dtAbout.html", {"request": request ,"pageid": pageid})
@dtRouter.get("/about/me", tags=["about"])
async def return_me():
    return dtMeta.return_me("about")

#<<>><<>><<>><<>>
# Header App navigation
#<<>><<>><<>><<>>
@dtRouter.get("/jupyterlab", tags=["headnav"])
async def jupyterlab(request: Request):
	return templates.TemplateResponse("jupyterlab.html", {"request": request})
@dtRouter.get("/jupyterlab/me", tags=["headnav"])
async def return_me():
    return dtMeta.return_me("jupyterlab")