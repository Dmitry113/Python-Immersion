# Задание №2
#
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.


from typing import Callable
import logging

logging.basicConfig(filename='info.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def my_logger(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        info_dict = {'args': args, **kwargs, 'result': result}
        logger.info(info_dict)
        return result

    return wrapper


@my_logger
def get_all(num1: int, *args, **kwargs) -> int:
    return num1


if __name__ == '__main__':
    get_all(5, 2, 3, 'str', x=5, y=8)
