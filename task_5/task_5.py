# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. В процессе сбора сохраните данные в текстовый файл используя
# логирование.

from pathlib import Path
import logging
import argparse
from collections import namedtuple

logging.basicConfig(filename='data_path.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

Files = namedtuple('File', 'name extension dir parent')

def read_dir(file: Path):
    file = Path(file)
    for file in file.iterdir():
        obj = Files(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(str(obj))
        if obj.dir:
            read_dir(Path(obj.parent) / obj.name)

def walker():
    my_walker = argparse.ArgumentParser(
        description='my_walker',
        prog='read_dir()',
    )
    my_walker.add_argument('-p', '--path', help='Введите полный путь до директории: ')
    args = my_walker.parse_args()
    return read_dir(args.path)

if __name__ == '__main__':
    walker()