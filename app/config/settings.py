import logging
import sys
from config import get_type_of_device

# Максимально подробный вывод логов
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')

# Нормальный вывод логов
formatter = logging.Formatter(fmt='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d.%m-%H:%M')

# Настройка вывода данных в файлы
system_handler = logging.FileHandler('system_data.log')
system_handler.setFormatter(formatter)

user_handler = logging.FileHandler('user_data.log')
user_handler.setFormatter(formatter)


def main():
    if get_type_of_device() == "Laptop":
        logging.basicConfig(
            format='[%(levelname)s] %(asctime)s - %(message)s',
            datefmt='%d.%m-%H:%M',
        )

        # Настройка внутренних логгеров
        system_logger = logging.getLogger('system_logging')
        system_logger.setLevel(logging.DEBUG)
        system_logger.addHandler(system_handler)
    else:
        # Настройка внутренних логгеров
        system_logger = logging.getLogger('system_logging')
        system_logger.setLevel(logging.INFO)
        system_logger.addHandler(system_handler)

    apscheduler_logger = logging.getLogger('apscheduler')
    apscheduler_logger.setLevel(logging.DEBUG)
    apscheduler_logger.addHandler(system_handler)

    aiogram_logger = logging.getLogger('aiogram')
    aiogram_logger.setLevel(logging.DEBUG)
    aiogram_logger.addHandler(system_handler)

    user_logger = logging.getLogger('user_logging')
    user_logger.setLevel(logging.DEBUG)
    user_logger.addHandler(user_handler)