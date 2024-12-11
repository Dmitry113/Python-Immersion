# Задание №6

# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.


import os
import logging
from collections import namedtuple

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="directory_info.log",
    filemode="a",
    encoding="utf-8"
)

# Определение структуры данных для хранения информации о файле или каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def gather_directory_info(directory_path):
    """
    Собирает информацию о содержимом директории и сохраняет ее в лог.
    """
    if not os.path.exists(directory_path):
        logging.error(f"Directory {directory_path} does not exist.")
        return

    logging.info(f"Gathering information for directory: {directory_path}")
    
    for root, dirs, files in os.walk(directory_path):
        parent_directory = os.path.basename(root)
        
        # Логируем информацию о каталогах
        for dir_name in dirs:
            dir_info = FileInfo(name=dir_name, extension=None, is_directory=True, parent_directory=parent_directory)
            logging.info(f"Directory: {dir_info}")
        
        # Логируем информацию о файлах
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            file_info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)
            logging.info(f"File: {file_info}")

def main():
    # Получаем путь директории от командной строки
    directory_path = input("Enter the directory path: ").strip()
    
    # Собираем информацию о содержимом директории
    gather_directory_info(directory_path)

if __name__ == "__main__":
    main()
