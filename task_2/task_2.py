# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.
from datetime import datetime


def main():
    now = datetime.now()
    formated_day = now.strftime('%Y-%m-%d %H:%M:%S')
    week_day = now.strftime('%A')
    number_of_week = now.isocalendar()[1]

    print(f'current day and time = {formated_day}')
    print(f'name of fay = {week_day}')
    print(f'number of week = {number_of_week}')

if __name__ == '__main__':
    main()