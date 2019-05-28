import csv


def import_data():
    cook_book = list()
    
    with open('cook_book.csv', encoding='UTF-8', newline='') as csvfile:
        cook_book_reader = csv.DictReader(csvfile, delimiter=';')
        
        for row in cook_book_reader:
            dish_dict = dict()
            ingridients_list = list()
            
            dish_dict['dish'] = row['dish']
            ingridients_quantity = int(row['ingridients_quantity'])
            dish_dict['ingridients_quantity'] = ingridients_quantity
            
            for i in range(ingridients_quantity):
                ingridient_dict = dict()
                
                ingridient_characteristic = row[None][i].split(' | ')
                ingridient_dict['ingridient_name'] = ingridient_characteristic[0]
                ingridient_dict['quantity'] = int(ingridient_characteristic[1])
                ingridient_dict['measure'] = ingridient_characteristic[2]
                ingridients_list.append(ingridient_dict)
            
            dish_dict['ingridients'] = ingridients_list
            cook_book.append(dish_dict)

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = import_data()
    shop_list = {}
    
    for dish in dishes:
        dish_index = list(filter(lambda x: cook_book[x]['dish'] == dish,
                                 range(len(cook_book))))[0]
        for ingridient in cook_book[dish_index]['ingridients']:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']
                ] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']
                ]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(
            **shop_list_item))


def create_shop_list():
    dishes = input("Введите названия блюд(а) на одного человека (в точности "
                   "как в файле cook_book.txt, разделяя пробелами): ").lower().split()
    person_count = int(input("Введите количество человек: "))
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()

input("Для выхода нажмите Enter")
'''Команда нужна для того, чтобы окно консоли
не закрылось сразу после выполнения программы в случае запуска файла с проводника
или файлового менеджера.'''