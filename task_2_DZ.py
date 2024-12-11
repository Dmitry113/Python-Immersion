# Задача 2.
#
# Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.


from datetime import datetime


def display_current_datetime():
    # Получение текущего времени и даты
    now = datetime.now()
    # Форматирование даты и времени
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    # Получение дня недели и номера недели
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]
    print(f'Current date and time: {formatted_date}')
    print(f'Day of the week: {day_of_week}')
    print(f'Week number: {week_number}')


if __name__ == '__main__':
    display_current_datetime()
