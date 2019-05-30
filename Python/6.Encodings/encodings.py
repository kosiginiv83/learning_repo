import json
import chardet


def file_load(file):
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        return json.loads(s)


def form_data_structure(files_list, chars_more):
    data_list = list()
    for file in files_list:
        words_dict = dict()
        news_dscrptns = list()
        news_dict = file_load(file)
        news_desc_list = news_dict['rss']['channel']['items']
        for i in range(len(news_desc_list)):
            words_list = news_desc_list[i]['description'].split(' ')
            words_list_condition = [word for word in words_list if
                                    len(word) > chars_more]
            news_dscrptns += words_list_condition
        words_dict['file'] = file
        words_dict['news'] = news_dscrptns
        data_list.append(words_dict)
    print("\nТоп 10 часто встречающихся слов, длиннее {} "
          "символов:".format(chars_more))
    top_ten_words(data_list)


def top_ten_words(data_list):
    for data in data_list:
        print('\n\tFile: ', data['file'])
        words = data['news']
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        sorted_count_pairs = sorted(freq.items(), key=lambda x: x[1],
                                    reverse=True)
        top10 = sorted_count_pairs[:10]
        for word, freq in top10:
            print("Слово '{}' встретилось {} раз".format(word, freq))


# Второй аргумент - число символов в слове - в данном
# случае поиск идет по словам длиннее шести символов
# (начиная с семи символов).
form_data_structure(['newsafr.json', 'newscy.json', 'newsfr.json',
                     'newsit.json'], 6)
# Программа работает корректно при значении данного
# параметра не более 9.