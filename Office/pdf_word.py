from pdf2docx import parse
import fnmatch
import os

def all_pdf_word():
    for file in os.listdir():
        if fnmatch.fnmatch(file, '*.pdf'):
            cv=parse(file,f"{file[:-4]}.docx")
            print(f'Файл "{file}" успешно преобразован!')
    return "Good"

def pdf_word(file):
    if fnmatch.fnmatch(file, '*.pdf'):
        cv = parse(file,f"{file[:-4]}.docx")
        print(f'Файл "{file}" успешно преобразован!')
    return 0

def dir_files_pdf():
    files=os.listdir()
    k=1
    for i in files:
        if fnmatch.fnmatch(i, '*.pdf'):
            print(f"[{k}]", i)
            k+=1
    print(f"Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога"
          f" введите: 0)\n")
    name_intput=input()
    try:
        try:
            name_intput=int(name_intput)
            if name_intput==0:
                all_pdf_word()
            else:
                pdf_word(files[name_intput-1])
        except IndexError:
            print("Такого значения нету")
    except ValueError:
        if name_intput in files:
            pdf_word(name_intput)
        else:
            print("Некоректно введёно имя файла!")
            return dir_files()
    return



