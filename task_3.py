# Задание №3

# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

from typing import Callable
import logging

# Настройка логирования
logging.basicConfig(
    filename='info.log', 
    filemode='a', 
    encoding='utf-8', 
    level=logging.INFO,
    format="%(levelname)s - %(asctime)s - %(message)s"
)
logger = logging.getLogger(__name__)

def my_logger(func: Callable):
    def wrapper(*args, **kwargs):
        # Получаем имя функции
        function_name = func.__name__
        # Вызываем оригинальную функцию
        result = func(*args, **kwargs)
        # Формируем информацию для записи в лог
        info_dict = {
            'function': function_name,
            'args': args,
            'kwargs': kwargs,
            'result': result
        }
        # Логируем информацию с детализированным выводом
        logger.info(f"Function: {info_dict['function']}, Arguments: {info_dict['args']}, "
                    f"Keyword Arguments: {info_dict['kwargs']}, Result: {info_dict['result']}")
        return result

    return wrapper


@my_logger
def get_all(num1: int, *args, **kwargs) -> int:
    return num1


if __name__ == '__main__':
    # Пример вызова функции
    get_all(5, 2, 3, 'str', x=5, y=8)
    


