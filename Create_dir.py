import os

#if __name__ == '__main__':
dir_name = input('Введите имя директории: ')

dir_path = os.path.join(os.getcwd(), dir_name)

try:
    os.mkdir(dir_path)
    print('Папка создана')
except FileExistsError:
    print('Такая директория уже существует')