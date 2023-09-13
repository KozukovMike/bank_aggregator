import logging

# Настройка корневого логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', encoding='utf-8')

# Создание и настройка логгера для logger_pars_errors
logger_pars_errors = logging.getLogger('logger_pars_errors')
handler1 = logging.FileHandler('errors.log', encoding='utf-8')
handler1.setLevel(logging.ERROR)
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

