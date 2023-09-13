from pydantic import BaseModel
from dataclasses import dataclass


@dataclass
class Cards:
    bank: str
    name: str
    info: str
    link: str


@dataclass
class Credits:
    bank: str
    name: str
    info: str
    link: str


@dataclass
class Insurance:
    bank: str
    name: str
    info: str
    link: str


@dataclass
class Deposits:
    bank: str
    name: str
    info: str
    link: str
