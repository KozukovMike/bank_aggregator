import secrets
import string
import bcrypt
import re


def generate_random_password(length: int = 12) -> str:
    """
    generate a random password of a given length
    :param length:
    :return: password
    """
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def hash_password(password: str) -> str:
    """
    function to hash a password
    :param password:
    :return:
    """
    salt = bcrypt.gensalt()
    entered_password = password.encode('utf-8')
    password_hash = bcrypt.hashpw(entered_password, salt)
    return password_hash.decode('utf-8')


def check_password(entered_password: str, password_hash: str) -> bool:
    """
    function to check if a password is correct
    :param entered_password:
    :param password_hash:
    :return:
    """
    entered_password = entered_password.encode('utf-8')
    if bcrypt.checkpw(entered_password, password_hash.encode('utf-8')):
        return True


def is_valid_email(email: str) -> bool:
    """
    check if an email is valid
    :param email: 
    :return: 
    """""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
