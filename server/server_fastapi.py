from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')



@app.get('/ping')
async def pong():
    return {'ping': 'pong'}

@app.get('/')
async def root(request: Request):
#     login form возможно не надо
    return templates.TemplateResponse("login_form.html", {"request": request})

