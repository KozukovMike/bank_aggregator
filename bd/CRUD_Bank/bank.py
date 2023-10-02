from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from models.bd_models import create_session, Bank


class CRUDBank:

    @staticmethod
    @create_session
    def add(instance, session=None):
        session.add(instance)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(instance)
            return instance

    @staticmethod
    @create_session
    def get(instance_id, session=None):
        instance = session.execute(
            select(Bank)
            .where(Bank.id == instance_id)
        )
        instance = instance.first()
        if instance:
            return instance[0]

    @staticmethod
    @create_session
    def get_by_bank(instance, session=None):
        instance = session.execute(
            select(Bank)
            .where(Bank.name == instance)
        )
        instance = instance.first()
        if instance:
            return instance[0]

    @staticmethod
    @create_session
    def all(session=None):
        instances = session.execute(
            select(Bank)
            .order_by(Bank.id)
        )
        return [i[0] for i in instances]

    @staticmethod
    @create_session
    def update(instance, session=None):
        instance = instance.__dict__
        del instance['_saUrl_instance_state']
        session.execute(
            update(Bank)
            .where(Bank.id == instance['id'])
            .values(**instance)
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def delete(instance_id, session=None):
        session.execute(
            delete(Bank)
            .where(Bank.id == instance_id)
        )
        session.commit()
