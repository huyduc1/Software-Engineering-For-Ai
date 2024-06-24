from fastapi import FastAPI, Request
from routers.user import user
from routers.summary import summary
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(user)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("service.html", 
                                      {"request": request, "name": "Hello world"})
