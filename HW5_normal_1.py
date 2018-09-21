import HW5_easy_2 #список директорий
#import Create_dir
#import Delete_dir
import os

def list_of_dir (HW5_easy_2_module):
    return HW5_easy_2_module.list_of_dir #список директорий

#def create_dir (Create_dir_module):
#    Create_dir_module.dir_name = input('Введите имя папки: ')

while True:
    print('Текущая дирректория: {}'.format(os.getcwd()))
    print('Меню:')
    print('1. Перейти в папку')
    print('2. Посмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    print('5. Выход')
    response = input('Выберите пункт: ')

    print()

    if response == '1':
        try:
            dir_1 = input('Имя папки: ')
            os.chdir(os.path.join(os.getcwd(), dir_1))
            print('Текущая дирректория: {}'.format(os.getcwd()))
            print('Список папок: {}'.format(HW5_easy_2.list_of_dir))
        except FileNotFoundError:
            print('Такой папки не существует')
    elif response == '2':
        print('Список папок: {}'.format(HW5_easy_2.list_of_dir))
    elif response == '3':
        import Delete_dir
    elif response == '4':
        import Create_dir
    elif response == '5':
        break
    else:
        print('Неверный ввод.')

    print()