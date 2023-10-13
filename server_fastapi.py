import uvicorn
from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from apscheduler.schedulers.background import BackgroundScheduler
from bd.CRUD_USERS.users import CRUDUser
from models.bd_models import User, UserRoleAssociation
from bd.CRUD_USERS.user_role_association import CRUDUserRoleAssociation
from bd.CRUD_USERS.roles import CRUDRole
from loggs.loggers import logger_server
from helpful_functions.password_functions import (generate_random_password, hash_password, check_password,
                                                  is_valid_email, is_valid_password)
from helpful_functions.bd_conn_functions import get_user_from_bd, create_admin, create_manager, create_user


app = FastAPI()
scheduler = BackgroundScheduler()
templates = Jinja2Templates(directory='templates')


def create_main_roles() -> None:
    admin_password = generate_random_password(20)
    manager_password = generate_random_password(20)
    print(manager_password, admin_password)
    create_admin(password=hash_password(password=admin_password), email='kozukovmisa@gmail.com')
    create_manager(password=hash_password(password=manager_password), email='kozukovmisa1@gmail.com')


@app.on_event("startup")
def start_scheduler():
    create_main_roles()
    scheduler.start()


@app.on_event("shutdown")
def shutdown_scheduler():
    scheduler.shutdown()


@app.get('/', response_class=HTMLResponse)
async def welcome_page(request: Request):
    return templates.TemplateResponse("welcome_page.html", {"request": request})


@app.get('/ping')
async def pong():
    return {'ping': 'pong'}


@app.post('/ping')
async def pong():
    return {'ping': 'pong'}


@app.get('/sign_up/', response_class=HTMLResponse)
async def sign_up_(request: Request):
    return templates.TemplateResponse("sign_up_form.html", {"request": request})


@app.post("/sign_up/")
async def sign_up(username: Annotated[str, Form()], password: Annotated[str, Form()], email: Annotated[str, Form()]):
    response = {}

    if not is_valid_password(password=password):
        response['password'] = 'Пароль неправильный. Пароль должен содержать минимум 8 символов, включая цифры и заглавные буквы.'
    elif not is_valid_email(email=email):
        response['email'] = 'Email неправильный.'
    if CRUDUser.get_by_username(instance=username):
        response['username'] = 'Такой пользователь уже существует.'
    if CRUDUser.get_by_email(instance=email):
        response['email'] = 'Этот email уже используется.'
    if not response:
        password_hash = hash_password(password=password)
        create_user(password_hash=password_hash, username=username, email=email)
        return {'message': 'Успешная регистрация'}
    return {'errors': response}


@app.get('/sign_in/', response_class=HTMLResponse)
async def sign_in_(request: Request):
    return templates.TemplateResponse("sign_in_form.html", {"request": request})


@app.post("/sign_in/")
async def sign_in(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    user = get_user_from_bd(username=username)
    if user is None:
        return {'message': 'такого пользователя не существует'}
    if not check_password(entered_password=password, password_hash=user.password_hash):
        return {'message': 'неверный пароль'}
    return {'message': 'Успешная аутентификация'}


@app.get('/forgot_password/', response_class=HTMLResponse)
async def forgot_new_password_(request: Request):
    return templates.TemplateResponse("forgot_password_form.html", {"request": request})


@app.post("/forgot_password/")
async def forgot_new_password(email: Annotated[str, Form()]):
    return {'message':  'Новый пароль отправлен на email'}


if __name__ == '__main__':
    uvicorn.run(app='server_fastapi:app', host='127.0.0.1', port=8000,  reload=True)
