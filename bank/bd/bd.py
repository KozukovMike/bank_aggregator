import psycopg2
import pandas as pd
from dotenv import load_dotenv
from abc import ABC, abstractmethod
from typing import List, Iterable, Any

from bank.loggs.loggers import logger_bd, logger_done_pars
from bank.bd.CRUD.bank import CRUDBank
from bank.bd.CRUD.card import CRUDCard
from bank.bd.CRUD.credit import CRUDCredit
from bank.bd.CRUD.insurance import CRUDInsurance
from bank.bd.CRUD.deposit import CRUDDeposit
from bank.models.bd_models import Bank, Card, Credit, Insurance, Deposit
from bank.models.bank_data_models import Deposits


load_dotenv()


class DBClient(ABC):

    @staticmethod
    @abstractmethod
    def to_bd(instances: Iterable[Any]) -> None:
        pass

    @staticmethod
    @abstractmethod
    def from_bd(table_name: str) -> pd.DataFrame:
        pass


class PostgresClient(DBClient):

    @staticmethod
    def to_bd(instances: Iterable[Any]) -> None:
        try:
            for instance in instances:
                class_name = instance.__class__.__name__
                bank_id = CRUDBank.get_by_bank(instance=instance.bank).id
                class_instance = globals()[f'{class_name}'[:-1]](
                    name=instance.name,
                    info=instance.info,
                    link=instance.link,
                    bank_id=bank_id,
                )
                globals()[f'CRUD{class_name}'[:-1]].add(instance=class_instance)
        except Exception as e:
            print(e)
            logger_bd.error(f'PostgresClient.to_bd: error: {e}')
