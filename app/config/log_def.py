import logging


def set_func(function: str, tag: str, status: str = "info"):
    if status == "info":
        logging.info(f"[%s] Вызвана функция: {function}", tag)
    elif status == "debug":
        logging.debug(f"[%s] Вызвана функция: {function}", tag)


def set_func_and_person(function, tag, message, status="info"):
    result = f"[%s] Вызвана функция: ({function}) пользователем: @{message.chat.username}/{message.chat.id}"
    if status == "info":
        logging.info(result, tag)
    elif status == "debug":
        logging.debug(result, tag)


def set_inside_func(data, function, tag, status="info"):
    if status == "info":
        logging.info(f"[%s] [%s]: {data}", tag, function)
    elif status == "debug":
        logging.debug(f"[%s] [%s]: {data}", tag, function)


def send_log(message, username, status="info"):
    if status == "info":
        logging.info(f"Пользователь: @{username} отправил сообщение {message}")
    elif status == "debug":
        logging.debug(f"Пользователь: @{username} отправил сообщение {message}")
