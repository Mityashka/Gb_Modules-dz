import argparse

def parse():
    parser = argparse.ArgumentParser(description='parser')
    parser.add_argument('number', type=int, help='Число для вывода')
    parser.add_argument('text', type=str, help='Строка для вывода')
    parser.add_argument('-v', '--verbose', action='store_true', help='Включить дополнительную информацию')
    parser.add_argument('-r', '--repeat', type=int, default=1, help='Количество повторений строки в выводе')
    args = parser.parse_args()

    if args.verbose:
        print(f'Получено число: {args.number}')
        print(f'Получена строка: {args.text}')
        print(f'Количество повторений: {args.repeat}')

    for i in range(args.repeat):
        print(args.text)

if __name__ == '__main__':
    parse()
