from bd.settings import DATABASE_URL
from bd.CRUD_Bank import CRUDBank, CRUDCard, CRUDCredit, CRUDDeposit, CRUDInsurance
from bd.CRUD_USERS import CRUDUser, CRUDRole, CRUDUserRoleAssociation
from models.bd_models import Bank, Card, Credit, Deposit, Insurance, Role, User, UserRoleAssociation


def get_user_from_bd(username: str) -> User | None:
    """
    get an instance of User from bd by username
    :param username:
    :return:
    """
    user = CRUDUser.get_by_username(instance=username)
    if isinstance(user, User):
        return user
    return None


def create_user(username: str, password_hash: str, email: str) -> None:
    """
    create and add to bd a new user instance, and give him a role 'user'
    :param username:
    :param password_hash:
    :param email:
    :return:
    """
    user = User(
        username=username,
        password_hash=password_hash,
        email=email
    )
    CRUDUser.add(instance=user)
    user_id = CRUDUser.get_by_username(instance=username).user_id
    ura = UserRoleAssociation(
        user_id=user_id,
        role_id=3
    )
    CRUDUserRoleAssociation.add(instance=ura)


def create_admin(password: str, email: str) -> None:
    """
    create and add to bd a new user instance, and give him a role 'admin'
    :return:
    """
    admin = User(
        username='admin',
        password_hash=password,
        email=email
    )
    CRUDUser.add(instance=admin)
    user_id = CRUDUser.get_by_username(instance='admin').user_id
    role_id = CRUDRole.get_by_name(instance_name='admin').role_id
    ura = UserRoleAssociation(
        user_id=user_id,
        role_id=role_id,
    )
    CRUDUserRoleAssociation.add(instance=ura)


def create_manager(password: str, email: str) -> None:
    """
    create and add to bd a new user instance, and give him a role 'manager'
    :return:
    """
    manager = User(
        username='manager',
        password_hash=password,
        email=email
    )
    CRUDUser.add(instance=manager)
    user_id = CRUDUser.get_by_username(instance='manager').user_id
    role_id = CRUDRole.get_by_name(instance_name='manager').role_id
    ura = UserRoleAssociation(
        user_id=user_id,
        role_id=role_id,
    )
    CRUDUserRoleAssociation.add(instance=ura)
