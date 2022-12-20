from docx2pdf import convert
import fnmatch
import os

def all_word_pdf():
    for file in os.listdir():
        if fnmatch.fnmatch(file, '*.docx'):
            cv=convert(file)
            file=f"{file[:-5]}.pdf"
    return "Good"

def word_pdf(file):
    if fnmatch.fnmatch(file, '*.docx'):
        convert(file)
        file = f"{file[:-5]}.pdf"
    return 0

def dir_files_docx():
    files=os.listdir()
    files=fnmatch.filter(files,"*.docx")
    k=1
    for i in files:
        if fnmatch.fnmatch(i, '*.docx'):
            print(f"[{k}]", i)
            k+=1
    print(f"Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога"
          f" введите: 0)\n")
    name_intput=input()
    try:
        try:
            name_intput=int(name_intput)
            if name_intput==0:
                all_word_pdf()
            else:
                word_pdf(files[name_intput-1])
        except IndexError:
            print("Такого значения нету")
    except ValueError:
        if name_intput in files:
            word_pdf(name_intput)
        else:
            print("Некоректно введёно имя файла!")
            return dir_files()
    return 0

