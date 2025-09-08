import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from storage import tasks

router = APIRouter(prefix="/pages", tags=["Фронтенд"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@router.get("/tasks")
async def get_tasks_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})
# print("✅ pages.py loaded")
