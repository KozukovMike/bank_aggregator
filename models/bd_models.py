from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, create_engine, Text, Float, String, Date, UniqueConstraint
from bd.settings import DATABASE_URL


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


class User(Base):
    __tablename__: str = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(255), nullable=False, unique=True)
    password_hash = Column(VARCHAR(255), nullable=False)


class Role(Base):
    __tablename__ = 'roles'

    role_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)


class UserRoleAssociation(Base):
    __tablename__ = 'user_role_association'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    __table_args__ = (
        UniqueConstraint('user_id', 'role_id', name='uq_user_role'),
    )


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(session=session, **kwargs)
    return wrapper


