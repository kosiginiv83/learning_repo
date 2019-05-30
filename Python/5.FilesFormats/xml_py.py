import xml.etree.ElementTree as ET


def import_data():
    dishes = list()
    
    tree = ET.parse('cook_book.xml')
    root = tree.getroot()
    dishes_raw = root.findall('dish')
    
    for index, dish in enumerate(dishes_raw):
        ingridients = list()
        one_dish = dict()
        
        dish_characteristic = dish.find('ingridients')
        dish_name = dish.attrib['dish_name']
        ingridients_quantity = dish_characteristic.attrib['ingridients_quantity']
        ingridients_raw = dish_characteristic.findall('ingridient')
        
        for ingridient in ingridients_raw:
            ingridients.append(ingridient.attrib)
        
        one_dish['dish'] = dish_name
        one_dish['ingridients_quantity'] = ingridients_quantity
        one_dish['ingridients'] = ingridients
        
        dishes.append(one_dish)
    
    for dish in dishes:
        for ingridient_list in dish['ingridients']:
            ingridient_list['quantity'] = int(ingridient_list['quantity'])
            
    return dishes


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = import_data()
    shop_list = {}
    for dish in dishes:
        dish_index = list(filter(lambda x: cook_book[x]['dish'] ==
                                           dish, range(len(cook_book))))
        dish_index = dish_index[0]
        for ingridient in cook_book[dish_index]['ingridients']:
            new_shop_list_item = ingridient
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['name'] not in shop_list:
                shop_list[new_shop_list_item['name']
                ] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['name']
                ]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{name} {quantity} {measure}'.format(
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