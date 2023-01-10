"""
    Объединить файлы в один файлы по следующим правилам:
    1. Содержимое исходных файлов в результирующем файле доллжно быть
        отсортировано по количеству строк в них
        (т.е. первым нужно записать файл с наименьшим количеством строк,
        а с последним - с наибольшим)
    2. Содержимое файла должно предваряться служебной информацией
        на 2-х строках: имя файла и количество строк в нем
"""


import os


list_files = [i for i in os.listdir() if i.endswith('.txt')]
list_files.sort()

try:
    with open('result.txt', 'a') as file_object:
        for line in list_files:
            print(line)
            files = open(line).readlines()
            file_object.write('\nФайл: ' + line +'\nКоличество строк: '
                              + str(len(files)) + '\n')
            for text in open(line):
                file_object.write(text)
                print(text)

except FileNotFoundError:
    print('Sorry, the file does not exist.')