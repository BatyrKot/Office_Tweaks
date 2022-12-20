import os
from PIL import Image

def compress(img_name: str, q: int):
    img_file = Image.open(img_name)
    img_file.save(img_name, quality=q)
    print(f'Файл "{img_name}" успешно преобразован!')


def image_files():
    i_files = os.listdir()
    i_fs=[]
    k=0

    for filename in i_files:
        if filename.endswith(('.jpg', '.jpeg', '.gif', '.png')):
            print(f'{k + 1}. {filename}')
            k+=1
            i_fs.append(filename)

    chosen_file_id = int(
        input(
            'Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0: '))
    quality = int(input('Введите параметры сжатия (от 0% до 100%): '))

    if chosen_file_id not in range(0, len(i_files) + 1) or quality not in range(0, 101):
        print('Неверный номер')
        return

    if chosen_file_id == 0:
        for j in range(0, len(i_fs)):
            compress(i_fs[j], quality)
    else:
        compress(i_fs[chosen_file_id-1], quality)