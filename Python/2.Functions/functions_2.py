documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people():
    status = None
    document_number = input("Введите номер документа: ")
    for document in documents:
        if document_number and document_number in document['number']:
            status = 'Exist'
            name = document['name']
    
    if status == 'Exist':
        print("Документ принадлежит", name)
    else:
        print("Документа с таким номером не существует.")


def list_doc():
    for document in documents:
        print('{0} "{1}" "{2}"'.format(document['type'],
                                       document['number'], document['name']))


def shelf():
    status = None
    document_number = input("Введите номер документа: ")
    for shelf, documents_list in directories.items():
        if document_number and document_number in documents_list:
            status = 'Exist'
            shelf_number = shelf
    
    if status == 'Exist':
        print("Данный документ на", shelf_number, "полке.")
    else:
        print("Документа с таким номером не существует.")


def add():
    document_number = None
    while not document_number or document_number in [x['number'] for x in documents]:
        document_number = input('Введите номер нового документа, не совпадающий с существующими: ')
    document_type = None
    while not document_type:
        document_type = input("Введите тип нового документа: ")
    document_owner = None
    while not document_owner:
        document_owner = input("Введите имя владельца нового документа: ")
    
    shelf_number = None
    while shelf_number not in directories.keys():
        shelf_number = input("Введите номер полки для нового документа: ")
        if shelf_number not in directories.keys():
            print("Полки с данным номером не существует.")
    
    document = dict()
    document['type'] = document_type
    document['number'] = document_number
    document['name'] = document_owner
    documents.append(document)
    directories[shelf_number].append(document_number)


def delete():
    status = None
    document_number = input("Введите номер документа: ")
    for index, document in enumerate(documents):
        if document_number and document_number in document['number']:
            status = 'Exist'
            del_doc_number = document_number
            del_doc_index = index
    
    if status == 'Exist':
        documents.pop(del_doc_index)
        for shelf, documents_list in directories.items():
            if del_doc_number in documents_list:
                directories[shelf].remove(del_doc_number)
        print("Документ удален.")
    else:
        print("Документа с таким номером не существует.")


def move():
    status = None
    document_number = input("Введите номер документа: ")
    for document in documents:
        if document_number and document_number in document['number']:
            status = 'Exist'
            move_doc_number = document_number
    
    if status == 'Exist':
        for shelf, document_list in directories.items():
            if move_doc_number in document_list:
                shelf_number = shelf
        move_shelf_number = input("Введите номер полки, на которую "
                                  "нужно переместить документ: ")
        if move_shelf_number in directories.keys():
            if move_shelf_number != shelf_number:
                directories[shelf_number].remove(move_doc_number)
                directories[move_shelf_number].append(move_doc_number)
                print("Документ перемещен.")
            else:
                print("Документ уже на этой полке.")
        else:
            print("Полки с таким номером не существует.")
    else:
        print("Документа с таким номером не существует.")


def add_shelf():
    new_shelf = input("Введите номер новой полки: ")
    if new_shelf:
        if new_shelf not in directories.keys():
            directories[new_shelf] = list()
            print("Полка добавлена.")
        else:
            print("Полка с таким номером уже существует.")
    else:
        print("Не введен номеп полки")


choice = None
while choice != 'q':
    print("\nВведите '?' для справки, 'q' для выхода.")
    choice = input("Введите команду: ")
    if choice == '?':
        print("\nВведите 'p' для определения кому принадлежит документ. "
              "\nВведите 'l' для вывода списка документов"
              "\nВведите 's' для определения на какой полке находится документ."
              "\nВведите 'a', чтобы добавить новый документ."
              "\nВведите 'd', чтобы удалить документ."
              "\nВведите 'm', чтобы переместить документ на другую полку."
              "\nВведите 'as', чтобы добавить новую полку.")
    elif choice == 'p':
        people()
    elif choice == 'l':
        list_doc()
    elif choice == 's':
        shelf()
    elif choice == 'a':
        add()
    elif choice == 'd':
        delete()
    elif choice == 'm':
        move()
    elif choice == 'as':
        add_shelf()