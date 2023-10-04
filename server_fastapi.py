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
from helpful_functions.password_functions import generate_random_password, hash_password, check_password, is_valid_email


app = FastAPI()
scheduler = BackgroundScheduler()
templates = Jinja2Templates(directory='templates')


def create_admin() -> None:
    admin_password = generate_random_password(20)
    manager_password = generate_random_password(20)
    admin = User(
        username="admin",
        password_hash=admin_password,
        email='kozukovmisa@gmail.com'
    )
    CRUDUser.add(instance=admin)
    user_id = CRUDUser.get_by_username(instance='admin').user_id
    role_id = CRUDRole.get_by_name(instance_name='admin').role_id
    ura = UserRoleAssociation(
        user_id=user_id,
        role_id=role_id,
    )
    CRUDUserRoleAssociation.add(instance=ura)
    manager = User(
        username="manager",
        password_hash=manager_password,
        email='kozukovmisa1@gmail.com'
    )
    CRUDUser.add(instance=manager)
    user_id = CRUDUser.get_by_username(instance='manager').user_id
    role_id = CRUDRole.get_by_name(instance_name='manager').role_id
    ura = UserRoleAssociation(
        user_id=user_id,
        role_id=role_id,
    )
    CRUDUserRoleAssociation.add(instance=ura)


@app.on_event("startup")
def start_scheduler():
    create_admin()
    scheduler.start()


@app.on_event("shutdown")
def shutdown_scheduler():
    scheduler.shutdown()


@app.get('/')
async def index():
    return {'dd': 'dd'}


@app.get('/ping')
async def pong():
    return {'ping': 'pong'}


@app.get('/login/')
async def login_page(request: Request):
    return templates.TemplateResponse("login_form.html", {"request": request})


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()], email: Annotated[str, Form()]):
    if is_valid_email(email=email):
        return {'message': 'email is correct'}
    if username == "1" and password == "1":
        return {"message": "Успешная аутентификация"}
    else:
        return {"message": "Неудачная аутентификация"}


# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     if username == "1" and password == "1":
#         return {"message": "Успешная аутентификация"}
#     else:
#         return {"message": "Неудачная аутентификация"}


# if __name__ == '__main__':
#     uvicorn.run(app='server_fastapi:app', host='0.0.0.0', port=8000,  reload=True)

