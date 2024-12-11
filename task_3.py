# Задание №3

# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging
from functools import wraps

# Настройка логгирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="function_calls.log",
    filemode="a"
)
logger = logging.getLogger("function_logger")

def log_function_call(func):
    """
    Декоратор для логирования вызовов функции, её аргументов и результата работы.
    Логируются раздельно:
    - уровень логирования
    - дата события
    - имя функции
    - аргументы вызова
    - результат
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Выполнение оригинальной функции
            result = func(*args, **kwargs)
            
            # Логируем информацию в требуемом формате
            logger.info(
                f"LEVEL: INFO\n"
                f"DATE: {logging.Formatter('%(asctime)s').format(logging.LogRecord('', '', '', '', '', '', '', ''))}\n"
                f"FUNCTION: {func.__name__}\n"
                f"ARGS: {args}, KWARGS: {kwargs}\n"
                f"RESULT: {result}\n"
            )
            return result
        except Exception as e:
            # Логируем исключение
            logger.error(
                f"LEVEL: ERROR\n"
                f"DATE: {logging.Formatter('%(asctime)s').format(logging.LogRecord('', '', '', '', '', '', '', ''))}\n"
                f"FUNCTION: {func.__name__}\n"
                f"ARGS: {args}, KWARGS: {kwargs}\n"
                f"ERROR: {e}\n"
            )
            raise

    return wrapper

# Пример использования
@log_function_call
def add(a, b):
    return a + b

@log_function_call
def divide(a, b):
    return a / b

if __name__ == "__main__":
    add(10, 20)
    try:
        divide(10, 0)  # Пример с делением на ноль
    except ZeroDivisionError:
        pass

