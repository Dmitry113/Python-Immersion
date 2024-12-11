# Задание №5

# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.


import logging
import argparse
from datetime import datetime, timedelta

# Настройка логгирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="date_parser.log",
    filemode="a"
)
logger = logging.getLogger("date_parser")

# Дни недели и месяцы на кириллице
weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
months = {
    "январь": 1, "февраль": 2, "март": 3, "апрель": 4, "май": 5, "июнь": 6,
    "июль": 7, "август": 8, "сентябрь": 9, "октябрь": 10, "ноябрь": 11, "декабрь": 12
}

def clean_text(text):
    """
    Очищает текст, заменяя некорректные символы.
    """
    try:
        text = text.encode('utf-8').decode('utf-8')
        return text
    except UnicodeDecodeError:
        logger.warning(f"Unable to decode text '{text}', returning original.")
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
        week_number_str = parts[0]  # Например, "1-й", "3-я"
        week_number = int(''.join(filter(str.isdigit, week_number_str)))  # Извлекаем только цифры из строки
        weekday_name = parts[1].lower()  # День недели в нижнем регистре
        month_name = parts[2].lower()  # Месяц в нижнем регистре

        # Преобразуем числовые значения для дней недели и месяцев в текст
        if weekday_name.isdigit():
            weekday_name = weekdays[int(weekday_name) - 1]  # Преобразуем число в день недели
        if month_name.isdigit():
            month_name = list(months.keys())[int(month_name) - 1]  # Преобразуем число в месяц

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

def get_default_values():
    """
    Возвращает значения по умолчанию для дня недели и месяца, если параметры не переданы.
    """
    today = datetime.now()
    weekday = weekdays[today.weekday()]
    month = list(months.keys())[today.month - 1]
    return weekday, month

def main():
    parser = argparse.ArgumentParser(description="Parse a weekday and month text to a specific date")
    parser.add_argument("week_number", nargs="?", type=int, default=1, help="Week number (default is 1)")
    parser.add_argument("weekday", nargs="?", type=str, default=None, help="Day of the week (default is the current weekday)")
    parser.add_argument("month", nargs="?", type=str, default=None, help="Month (default is the current month)")

    args = parser.parse_args()

    # Если значения не переданы, используем текущий день недели и месяц
    weekday, month = args.weekday, args.month
    if weekday is None or month is None:
        weekday, month = get_default_values()

    # Формируем строку для парсинга
    text = f"{args.week_number}-й {weekday} {month}"

    print(f"Parsing: {text}")
    result = parse_text_to_date(text)

    if result:
        print(f"Target date: {result.strftime('%d-%m-%Y')}")
    else:
        print(f"Failed to parse the input text: {text}")

if __name__ == "__main__":
    main()

