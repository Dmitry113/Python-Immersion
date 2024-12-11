# Задание №2

# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.


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
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Логируем аргументы функции
        logger.debug(f"Called {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        try:
            result = func(*args, **kwargs)  # Выполнение оригинальной функции
            # Логируем результат функции
            logger.debug(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            # Логируем исключения
            logger.error(f"Exception in {func.__name__}: {e}")
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
