"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
dict_int = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_3.txt', encoding='utf-8') as file_obj:

    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(dict_int[i[0]] + '  ' + i[1])
    print(new_file)

with open('text_3_new.txt', 'a') as file_obj_2:
    file_obj_2.writelines(new_file)