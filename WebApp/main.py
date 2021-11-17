from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import requests




templates = Jinja2Templates(directory='templates')

bot_name = "BOT"

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", )
async def index(request: Request):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    return templates.TemplateResponse("bot.html", {"request": request})
    
    #return templates.TemplateResponse("bot2.html", {"request": request, "bot_name": bot_name, "time_now": current_time})



@app.post("/chat", response_class=HTMLResponse)
async  def chat(request: Request):
    form_data = await request.form()
    
    param = {
        "sender": "test",
        "message": form_data['text']
    }
    response = requests.post("http://localhost:5055", json=param)
    response = response.json()
    print(response)
    response_text = response[0]['text']
    return JSONResponse({"status": "success", "response": response_text})