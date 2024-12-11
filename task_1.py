# Задание №1
#
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.


import logging

def setup_logging():
    # Создание логгера
    logger = logging.getLogger("multi_file_logger")
    logger.setLevel(logging.DEBUG)  # Установим минимальный уровень логгирования для логгера

    # Удаляем старые обработчики, чтобы избежать дублирования
    if logger.hasHandlers():
        logger.handlers.clear()

    # Создание обработчика для debug_info.log
    debug_info_handler = logging.FileHandler("debug_info.log")
    debug_info_handler.setLevel(logging.DEBUG)  # Логи DEBUG и INFO
    debug_info_handler.addFilter(lambda record: record.levelno <= logging.INFO)

    # Создание обработчика для warnings_errors.log
    warnings_errors_handler = logging.FileHandler("warnings_errors.log")
    warnings_errors_handler.setLevel(logging.WARNING)  # Логи WARNING и выше

    # Настройка формата сообщений
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    debug_info_handler.setFormatter(formatter)
    warnings_errors_handler.setFormatter(formatter)

    # Добавление обработчиков к логгеру
    logger.addHandler(debug_info_handler)
    logger.addHandler(warnings_errors_handler)

    return logger

if __name__ == "__main__":
    # Настройка логгирования
    logger = setup_logging()

    # Примеры логирования
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    
    try:
        result = 10 / 0  # Ошибка деления на ноль
    except ZeroDivisionError as e:
        logger.error(f"Division by zero error occurred: {e}")

    logger.warning("This is a warning message")
    logger.critical("This is a critical message")
