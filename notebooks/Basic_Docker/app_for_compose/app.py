import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import redis

app = FastAPI()

r = redis.Redis(
    host = os.getenv("REDIS_HOST","localhost"),
    port=6379,
    decode_responses=True
)
templates = Jinja2Templates(
    directory="templates"
)

@app.get("/",response_class=HTMLResponse)
def home(request: Request):
    messages = r.lrange("messages",0,-1)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "messages": messages[::-1]}
    )

@app.post("/add")
def add_message(message: str = Form(...)):
    r.lpush("messages", message)
    return RedirectResponse("/", status_code=303)
