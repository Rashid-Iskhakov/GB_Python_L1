import os

list_of_dir =  [x for x in os.listdir(path='.') if os.path.isdir(os.path.join(os.getcwd(), x))]

if __name__ == '__main__':
    print(list_of_dir)