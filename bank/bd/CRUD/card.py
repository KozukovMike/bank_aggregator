from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from bank.models.bd_models import create_session, Card

class CRUDCard:

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
            select(Card)
            .where(Card.id == instance_id)
        )
        instance = instance.first()
        if instance:
            return instance[0]

    @staticmethod
    @create_session
    def get_by_name(instance, session=None):
        instance = session.execute(
            select(Card)
            .where(Card.name == instance)
        )
        instance = instance.first()
        if instance:
            return instance[0]

    @staticmethod
    @create_session
    def all(session=None):
        instances = session.execute(
            select(Card)
            .order_by(Card.id)
        )
        return [i[0] for i in instances]

    @staticmethod
    @create_session
    def update(instance, session=None):
        instance = instance.__dict__
        del instance['_sa_instance_state']
        session.execute(
            update(Card)
            .where(Card.id == instance['id'])
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
            delete(Card)
            .where(Card.id == instance_id)
        )
        session.commit()
