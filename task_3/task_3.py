from datetime import datetime, timedelta


def main():
    now = datetime.now()
    next_days = int(input('Введите количество дней вперед: '))
    return (now + timedelta(days=next_days)).strftime('%Y-%m-%d')



if __name__ == '__main__':
    print(main())