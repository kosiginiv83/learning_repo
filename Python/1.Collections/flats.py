import csv

with open('output.csv', newline='', encoding='UTF-8') as csvfile:
    flat_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flat_csv)
# print(flats_list)


# TODO 1
# Напишите цикл, который проходит по всем квартирам, и печатает только новостройки и их порядковые номера в файле.
todo1_numbers = []
for i, flat in enumerate(flats_list):
    if 'новостройка' in flat:
        # print('\n', i, flat)
        todo1_numbers.append(i)
print('\n', todo1_numbers, 'Квартир:', len(todo1_numbers),
      'из', len(flats_list))

# TODO 2:
# При помощи пересечения множеств попробуйте сравнить больше двух новостроек между собой одновременно
flats_intersection = set(flats_list[1]) & set(flats_list[4]) & set(flats_list[5]) & set(flats_list[6])
print(flats_intersection)
print(type(flats_intersection))

# TODO 3:
# Вот так мы превратили наш массив квартир в словарь, где ключом является уникальный номер объявления,
# а значением - ссылка на страничку с объявлением.
# Измените код так, чтобы стало наоборот.
test_dict = dict()
for i, flat in enumerate(flats_list):
    if i == 0:
        continue
    #   test_dict[flat[0]] = flat[len(flat)-1]
    test_dict[flat[len(flat) - 1]] = flat[0]
# print(test_dict)
print(type(test_dict))

# Каждую квартиру представляем словарем с ключами из flats_list[0].
# Для удобства не включаем в словарь "Описание".
# Словари закидываем в список.
# В output.csv добавил: "Тип дома" между "Этажей" и "Цена"
# и пустое поле между "Лифт" и "Ссылка на объявление" - стало лучше
# (самые важные характеристики отображаются в соответствующих полях)
# но на некоторых квартирах наблюдается незначительное съезжание
# характеристик (нужно дальше разбираться с output.csv).
list_dict = list()
for i, flat in enumerate(flats_list):
    if i == 0:
        continue
    flat_dict = dict()
    for characteristic, value in zip(flats_list[0], flat):
        if characteristic != 'Описание':
            flat_dict[characteristic] = value
    list_dict.append(flat_dict)
# Выводим одну из квартир для контроля.
print('\n', list_dict[11])

# Рассчитаем среднюю цену за квартиры
prices = list()
for flat in list_dict:
    prices.append(int(flat['Цена']))
print("\nСредняя цена:", round(sum(prices) / len(prices)))
# print('\n', prices)


# Выведем на какой станции больше всего предложений
undergrounds = list()
num_offers = dict()
for flat in list_dict:
    undergrounds.append(flat['Метро'])
for underground in set(undergrounds):
    offer_count = undergrounds.count(underground)
    num_offers[underground] = offer_count
print('\n', num_offers)

# Вариант 1
max_offer = 0
for underground, offer_count in num_offers.items():
    if offer_count > max_offer:
        max_offer = offer_count
        max_underground = underground
print("\n(Вар.1) Больше всего предложений на:",
      max_underground, '-', max_offer)

# Вариант 2
underground_list = list()
offers_list = list()
for underground, offer_count in num_offers.items():
    underground_list.append(underground)
    offers_list.append(offer_count)
max_offer_value = max(offers_list)
max_underground_index = offers_list.index(max_offer_value)
print("\n(Вар.2) Больше всего предложений на:",
      underground_list[max_underground_index],
      '-', max_offer_value)

# Есть 27 предложений, где не указана станция метро,
# возможно, из-за них съезжают характеристики.
# Выведем эти предложения (ID).
print('\nНе указаны станции метро для:')
no_underground_ids = list()
no_underground_indexes = list()
for i, flat in enumerate(list_dict):
    if flat['Метро'] == '':
        no_underground_ids.append(flat['ID'])
        no_underground_indexes.append(i)
print(no_underground_ids)

# Выведем одну из квартир без метро.
print("\nОдна из квартир без указания станции метро", list_dict[no_underground_indexes[0]])
# Нет, не из-за них съезжают.