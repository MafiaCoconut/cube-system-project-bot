import logging
from app.config_reader import get_type_of_device
from dotenv import load_dotenv
import os

load_dotenv()
system_logger = logging.getLogger('system_logging')
user_logger = logging.getLogger('user_logging')


def set_func(function: str, tag: str, status: str = "info"):
    result = f"Called Tag:[{tag}] Function:({function})"
    if status == "info":
        system_logger.info(result)
    elif status == "debug":
        system_logger.debug(result)


def set_inside_func(data, function, tag, status="info"):
    result = f"[{tag}] [{function}]: {data}"
    if status == "info":
        system_logger.info(result)
    elif status == "debug":
        system_logger.debug(result)


def set_func_and_person(function, tag, message, status="info"):
    result = f"User: {message.chat.username}/{message.chat.id} Tag: [{tag}]  Function: ({function})"
    if status == "info":
        # logging.info(result, tag)
        user_logger.info(result)
    elif status == "debug":
        # logging.debug(result, tag)
        user_logger.debug(result)


def send_log(message):
    result = f'User: {message.chat.username}/{message.chat.id} Send Message: "{message.text}"'
    user_logger.info(result)


def add_or_delete_user(message, command):
    if command == "add":
        result = f'Add User: {message.chat.username}/{message.chat.id}'
    else:
        result = f'Delete User: {message.chat.username}/{message.chat.id}'

    user_logger.info(result)


def logs_settings():
    # Максимально подробный вывод логов
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')

    # Нормальный вывод логов
    formatter = logging.Formatter(fmt='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d.%m-%H:%M')

    # Настройка вывода данных в файлы
    system_handler = logging.FileHandler('system_data.log')
    system_handler.setFormatter(formatter)

    user_handler = logging.FileHandler('user_data.log')
    user_handler.setFormatter(formatter)

    global system_logger
    if os.getenv("DEVICE") == "Laptop":
        logging.basicConfig(
            format='[%(levelname)s] %(asctime)s - %(message)s',
            datefmt='%d.%m-%H:%M',
        )
        system_logger.setLevel(logging.DEBUG)
    else:
        system_logger.setLevel(logging.INFO)
    system_logger.addHandler(system_handler)

    apscheduler_logger = logging.getLogger('apscheduler')
    apscheduler_logger.setLevel(logging.DEBUG)
    apscheduler_logger.addHandler(system_handler)

    aiogram_logger = logging.getLogger('aiogram')
    aiogram_logger.setLevel(logging.DEBUG)
    aiogram_logger.addHandler(system_handler)

    global user_logger
    user_logger.setLevel(logging.DEBUG)
    user_logger.addHandler(user_handler)