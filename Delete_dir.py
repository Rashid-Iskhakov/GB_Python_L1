import os

#if __name__ == '__main__':
dir_name = input('Введите имя директории: ')
dir_path = os.path.join(os.getcwd(), dir_name)

try:
    os.rmdir(dir_path)
    print('Успешно удалено')
except FileExistsError:
    print('Директория {} не существует'.format(dir_name))