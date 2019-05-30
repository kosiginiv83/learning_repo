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


#  Программа ищет по содержимому файлов.
#  Работает только с текстовыми файлами.
import os
import chardet


def file_analyse(files_list, path):
    interim_list = list()
    
    user_input = input("Введите строку: ")
    for file in files_list:
        file_name, file_extension = os.path.splitext(file)
        if file_extension == '.sql':
            file_path = os.path.join(path, file)
            with open(file_path, 'rb') as f:
                data = f.read()
                result = chardet.detect(data)
                text = data.decode(result['encoding'])
                if user_input in text:
                    interim_list.append(file)
    
    for item in interim_list:
        print(os.path.join(migrations, item))
    print('Всего: ', len(interim_list))
    
    file_analyse(interim_list, path)


if __name__ == '__main__':
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, migrations)
    files_list = os.listdir(path)
    file_analyse(files_list, path)