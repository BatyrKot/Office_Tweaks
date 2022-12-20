import os

os.chdir(r"C:\Users\777\Down")

def delete_start(count: str):
    for file in os.listdir():
        if file.startswith(count):
            os.remove(file)

def delete_end(count: str):
    for file in os.listdir():
        if file.split('.')[0].endswith(count):
            os.remove(file)

def delete_with(count: str):
    for file in os.listdir():
        if file.count(count) > 0:
            os.remove(file)


def delete_ext(count: str):
    for file in os.listdir():
        if file.count('.') == 1 and file.split('.')[1] == count:
            os.remove(file)

def dir_files():
    files = os.listdir()
    k = 1
    for i in files:
        print(f"[{k}]", i)
        k += 1
    print('Выберите действие: \n')
    print('1. Удалить все файлы начинающиеся на определенную подстроку \n'
          '2. Удалить все файлы заканчивающиеся на определенную подстроку \n'
          '3. Удалить все файлы содержащие определенную подстроку \n'
          '4. Удалить все файлы по расширению')

    subcommand = int(input())
    count = input('Введите подстроку: ')
    if subcommand == 1:
        delete_start(count)
    elif subcommand == 2:
        delete_end(count)
    elif subcommand == 3:
        delete_with(count)
    elif subcommand == 4:
        delete_ext(count)
    else:
        print("Неверно введено значение!")

