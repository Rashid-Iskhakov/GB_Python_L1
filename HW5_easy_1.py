import os

n = 9
path_list = []

for i in range(n):

    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i + 1))
    path_list.append(dir_path)

    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

choise = input('Удалить созданные директории? (Y/N)' )

if choise == 'Y':

    for i in range(len(path_list)):

        try:
            os.rmdir(path_list[i])
        except FileExistsError:
            print('Дирректория {} не существует'.format(path_list[i]))