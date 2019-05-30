import chardet
import os
import requests


def translate_it(original_file, result_file, language, language_need='ru'):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/\
                translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    
    print(f'\nПожалуйста, подождите. Переводится файл:\n\t{original_file}')
    
    with open(original_file, 'rb') as f:
        data = f.read()
        cp = chardet.detect(data)
        text = data.decode(cp['encoding'])
    
    params = {
        'key': key,
        'text': text,
    }
    params['lang'] = language + '-' + language_need
    
    response = requests.get(url, params=params).json()
    if response['code'] != 200:
        print('Ошибка:', response['code'], response['message'])
        return

    tr_text = ' '.join(response.get('text', []))
    with open(result_file, 'w') as f:
        f.write(tr_text)


if __name__ == '__main__':
    prog_dir = os.path.dirname(os.path.abspath(__file__))
    original_dir = os.path.join(prog_dir, 'original')
    files_list = os.listdir(original_dir)
    result_dir = os.path.join(prog_dir, 'translated')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    for file in files_list:
        file_name, file_extension = os.path.splitext(file)
        language = file_name.lower()
        original_file = os.path.join(original_dir, file)
        result_file = os.path.join(result_dir, file)
        translate_it(original_file, result_file, language)
    
    print('\nРабота программы завершена.')