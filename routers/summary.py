from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

summary = APIRouter() 

templates = Jinja2Templates(directory="templates")

@summary.get("/")
async def index(request: Request):
    return templates.TemplateResponse("service.html", {"request": request})