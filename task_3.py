# Задание №3
#
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

from typing import Callable
import logging


FORMAT = '{levelname:<8} - {asctime}. {msg}'

logging.basicConfig(format=FORMAT, filename='info.log', filemode='a', style='{', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def my_logger(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        info_dict = {'args': args, **kwargs, 'result': result}
        logger.info(f'Функция - {func.__name__}(), аргументы: {info_dict}, результат - {result}')
        return result

    return wrapper


@my_logger
def get_all(num1: int, *args, **kwargs) -> int:
    return num1


if __name__ == '__main__':
    get_all(5, 2, 3, 'str', x=5, y=8)
