import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from apscheduler.schedulers.background import BackgroundScheduler
from bd.CRUD_USERS.users import CRUDUser
from models.bd_models import User, UserRoleAssociation
from bd.CRUD_USERS.user_role_association import CRUDUserRoleAssociation
from bd.CRUD_USERS.roles import CRUDRole
from loggs.loggers import logger_server


app = FastAPI()
scheduler = BackgroundScheduler()
templates = Jinja2Templates(directory='templates')


def create_admin() -> None:
    user = User(
        username="admin",
        password_hash=''
    )
    CRUDUser.add(instance=user)
    user_id = CRUDUser.get_by_username(instance='admin').user_id
    role_id = CRUDRole.get_by_name(instance_name='admin').role_id
    ura = UserRoleAssociation(
        user_id=user_id,
        role_id=role_id,
    )
    CRUDUserRoleAssociation.add(instance=ura)
    user = User(
        username="manager",
        password_hash=''
    )
    CRUDUser.add(instance=user)
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


@app.get('/ping')
async def pong():
    return {'ping': 'pong'}


@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse("login_form.html", {"request": request})


# if __name__ == '__main__':
#     uvicorn.run(app='server_fastapi:app', host='0.0.0.0', port=8000,  reload=True)

