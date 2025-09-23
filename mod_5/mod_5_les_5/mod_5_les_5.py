# Задание 1

from pathlib import Path
import os
import shutil


BASE_DIR = Path(__file__).parent
folder_path = BASE_DIR / 'Управление_файлами'

if not folder_path.exists():
    folder_path.mkdir()
    print(f'Папка "{folder_path.name}" создана')
else:
    print(f'Папка "{folder_path.name}" уже существует')

with open(folder_path / 'file1.txt', 'w', encoding='utf8') as f:
    f.write('Создание первого файла')

with open(folder_path / 'file2.txt', 'w', encoding='utf8') as f:
    f.write('Создание второго файла')

print(os.listdir(folder_path))

# Задание 2

os.remove(folder_path / 'file2.txt')

folder_path_inner = BASE_DIR / 'Управление_файлами'/ 'Управление_файлами_внутренняя'
folder_path_inner.mkdir()
os.rename(folder_path / 'file1.txt', folder_path_inner / 'file1.txt')  

shutil.rmtree(folder_path)