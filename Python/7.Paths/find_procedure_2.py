# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции


#  !!! Внимание: find_procedure_2.py ищется по всему диску,
#  ссылка на который в переменной окружения ОС 'HOMEDRIVE'.
#  find_procedure_2.py должен быть один на диске.

#  Программа ищет по названиям файлов
import os


# from pprint import pprint


def find_py_file():
    hdd = os.environ['HOMEDRIVE']
    for root, dirs, files in os.walk(hdd):
        for _file in files:
            if _file == 'find_procedure_2.py':
                py_dir = os.path.abspath(_file)
                return py_dir


migrations = 'Migrations'
file_dir = find_py_file()
current_dir = os.path.dirname(file_dir)


def sql_select():
    sql_files_list = list()
    
    files_dir = os.path.join(current_dir, migrations)
    files_list = os.listdir(files_dir)
    for file in files_list:
        file_name, file_extension = os.path.splitext(file)
        if file_extension == '.sql':
            sql_files_list.append(file)
    
    file_search(sql_files_list)


def file_search(sql_files_list):
    interim_list = list()
    
    user_input = input("Введите строку: ")
    for file in sql_files_list:
        if user_input in file:
            interim_list.append(file)
    
    for item in interim_list:
        print(os.path.join(migrations, item))
    print('Всего: ', len(interim_list))
    
    file_search(interim_list)


if __name__ == '__main__':
    sql_select()