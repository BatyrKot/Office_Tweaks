import os
from pdf_word import *
from word_pdf import *
from image_comress import *
from Delete import *

def menu():
    print(f"Текущий каталог: {os.getcwd()}")
    print("Выберите действия:")
    print("[0]-Сменить рабочий каталог \n"
          "[1]-Преобразовать PDF в Docx \n"
          "[2]-Преобразовать Docx в Pdf\n"
          "[3]-Сжать изображение\n"
          "[4]-Удалить файл\n"
          "[5]-Выход")
    choice=int(input())

    if choice==0:
        new_catalog=input("Введите новый каталог:")
        try:
            os.chdir(new_catalog)
        except FileNotFoundError:
            print("Такого каталога не существует")
    if choice==1:
        print(f"Список файлов с расширением .pdf в данном каталоге:\n")
        dir_files_pdf()
    if choice==2:

        print(f"Список файлов с расширением .docx в данном каталоге:\n")
        dir_files_docx()
    if choice==3:

        print('Список файлов с раширением (".jpeg", ".gif", ".png", ".jpg") в данном каталоге: \n')
        image_files()
    if choice==4:

        print('Список файлов, которые Вы можете удалить: \n')
        dir_files()
    elif choice == 5:
        return 0


