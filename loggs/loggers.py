import logging

# Настройка корневого логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', encoding='utf-8')

# Создание и настройка логгера для logger_pars_errors
logger_pars_errors = logging.getLogger('logger_pars_errors')
handler1 = logging.FileHandler('errors.log', encoding='utf-8')
handler1.setLevel(logging.INFO)
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler1.setFormatter(formatter1)
logger_pars_errors.addHandler(handler1)
logger_pars_errors.propagate = False


# Создание и настройка логгера для logger_done_pars
logger_done_pars = logging.getLogger('logger_done_pars')
handler2 = logging.FileHandler('done.log', encoding='utf-8')
handler2.setLevel(logging.INFO)
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler2.setFormatter(formatter2)
logger_done_pars.addHandler(handler2)
logger_done_pars.propagate = False


logger_bd = logging.getLogger('logger_bd')
handler3 = logging.FileHandler('bd.log', encoding='utf-8')
handler3.setLevel(logging.INFO)
formatter3 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler3.setFormatter(formatter3)
logger_bd.addHandler(handler3)
logger_bd.propagate = False

logger_server = logging.getLogger('logger_server')
handler4 = logging.FileHandler('server.log', encoding='utf-8')
handler4.setLevel(logging.INFO)
formatter4 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler4.setFormatter(formatter4)
logger_bd.addHandler(handler4)
logger_bd.propagate = False
