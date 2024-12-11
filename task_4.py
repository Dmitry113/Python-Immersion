# Задание №4

# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.


import logging
from datetime import datetime, timedelta

# Настройка логгирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="date_parser.log",
    filemode="a",
    encoding='utf-8'  # Указываем кодировку для записи в файл
)
logger = logging.getLogger("date_parser")

def clean_text(text):
    """
    Очищает текст, заменяя некорректные символы.
    """
    try:
        # В Python 3 строки уже работают с кодировкой Unicode, поэтому преобразование не нужно
        return text
    except Exception:
        # Если возникли проблемы с текстом, логируем предупреждение и возвращаем оригинал
        logger.warning("Unable to clean text, returning original.")
        return text

def parse_text_to_date(text):
    """
    Преобразует текст вида "1-й четверг ноября" в дату текущего года.
    Логирует ошибки, если текст не соответствует формату.
    """
    try:
        # Очищаем текст от возможных проблем с кодировкой
        text = clean_text(text)

        # Разбиваем строку на части
        parts = text.split()
        if len(parts) != 3:
            raise ValueError("Input text must be in the format '<number>-й <weekday> <month>'")

        # Извлекаем данные из текста
        week_number_str = parts[0]  # Например, "1-й", "3-й"
        week_number = int(''.join(filter(str.isdigit, week_number_str)))  # Извлекаем только цифры из строки
        weekday_name = parts[1].lower()  # День недели в нижнем регистре
        month_name = parts[2].lower()  # Месяц в нижнем регистре

        # Убираем окончания у названий месяцев
        month_name = month_name.split()[0]  # Убираем окончания месяца (например, "ноября" -> "ноябрь")

        # Сопоставление дней недели и месяцев (на кириллице)
        weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
        months = {
            "январь": 1, "февраль": 2, "март": 3, "апрель": 4, "май": 5, "июнь": 6,
            "июль": 7, "август": 8, "сентябрь": 9, "октябрь": 10, "ноябрь": 11, "декабрь": 12
        }

        if weekday_name not in weekdays:
            raise ValueError(f"Invalid weekday name: {weekday_name}")

        if month_name not in months:
            raise ValueError(f"Invalid month name: {month_name}")

        # Получаем номер дня недели и месяца
        weekday = weekdays.index(weekday_name)  # Понедельник = 0, ..., воскресенье = 6
        month = months[month_name]
        year = datetime.now().year

        # Находим первую дату месяца
        first_day = datetime(year, month, 1)
        first_weekday = first_day.weekday()

        # Рассчитываем смещение до нужного дня недели
        offset = (weekday - first_weekday) % 7
        first_target_weekday = first_day + timedelta(days=offset)

        # Рассчитываем нужную неделю
        target_date = first_target_weekday + timedelta(weeks=week_number - 1)

        if target_date.month != month:
            raise ValueError("Invalid week number for the given month")

        return target_date

    except Exception as e:
        logger.error(f"Error parsing text '{text}': {e}")
        return None

# Пример использования
if __name__ == "__main__":
    print(parse_text_to_date("1-й четверг ноябрь"))  # Пример корректного ввода
    print(parse_text_to_date("3-я среда май"))  # Пример корректного ввода
    print(parse_text_to_date("5-я среда февраля"))   # Пример некорректного ввода

