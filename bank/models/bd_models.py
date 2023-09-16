from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, create_engine, DATETIME, Text
from bank.bd.CRUD.settings import DATABASE_URL


Base = declarative_base()


class Bank(Base):
    __tablename__: str = 'bank'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False, unique=True)


class Credit(Base):
    __tablename__: str = 'credit'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False, unique=True)
    info = Column(Text)
    link = Column(VARCHAR(255))
    bank_id = Column(Integer, ForeignKey('bank.id', ondelete='CASCADE'), nullable=False)

class Card(Base):
    __tablename__: str = 'card'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False, unique=True)
    info = Column(Text)
    link = Column(VARCHAR(255))
    bank_id = Column(Integer, ForeignKey('bank.id', ondelete='CASCADE'), nullable=False)



class Insurance(Base):
    __tablename__: str = 'insurance'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False, unique=True)
    info = Column(Text)
    link = Column(VARCHAR(255))
    bank_id = Column(Integer, ForeignKey('bank.id', ondelete='CASCADE'), nullable=False)


class Deposit(Base):
    __tablename__: str = 'deposit'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False, unique=True)
    info = Column(Text)
    link = Column(VARCHAR(255))
    bank_id = Column(Integer, ForeignKey('bank.id', ondelete='CASCADE'), nullable=False)


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(session=session, **kwargs)
    return wrapper


