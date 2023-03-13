from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import dtServer.dtMain as dtMain

templates = Jinja2Templates(directory="dtServer/templates")

dtRouter = APIRouter()

#index begin
@dtRouter.get("/", tags=["root"])
async def dtroot():
    return {"app": "Data Tools", "Author": "Rei Ryu"}
@dtRouter.get("/me", tags=["root"])
async def read_root_me():
    return {"page": "Data Tools","Date": "22-11-2020" , "Author": "Rei Ryu"}
#index end
#main begin
@dtRouter.get("/main", response_class=HTMLResponse, tags=["main"])
async def main(request: Request):
	hello = dtMain.hello()
	return templates.TemplateResponse("template.html", {"request": request ,"id": id, "hello": hello})
@dtRouter.get("/main/me", tags=["main"])
async def read_main_me():
    return {"page": "main","Author": "Rei Ryu", "Date": "22-11-2020", "Last modified": "30-11-2020" }
#main end
#dashboard begin
@dtRouter.get("/dashboard", tags=["dashboard"])
async def dashboard():
    return {
    	"code: succes",
    	"message:" "dashboard created"}
@dtRouter.get("/dashboard/me", tags=["dashboard"])
async def read_dashboard_me():
    return {"page": tags ,"Author": "Rei Ryu"}
#dashboard end