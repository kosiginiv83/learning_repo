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
        if document_number in document['number']:
            status = 'Exist'
            name = document['name']
    
    if status == 'Exist':
        print("Документ принадлежит", name)
    else:
        print("Введенный номер документа не существует.")


def list():
    for document in documents:
        print('{0} "{1}" "{2}"'.format(document['type'],
                                       document['number'], document['name']))


def shelf():
    status = None
    document_number = input("Введите номер документа: ")
    for shelf, documents_list in directories.items():
        if document_number in documents_list:
            status = 'Exist'
            shelf_number = shelf
    
    if status == 'Exist':
        print("Данный документ на", shelf_number, "полке.")
    else:
        print("Введенный номер документа не существует.")


def add():
    document_number = input("Введите номер нового документа: ")
    document_type = input("Введите тип нового документа: ")
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


choice = None
while choice != 'q':
    print("\nВведите '?' для справки, 'q' для выхода.")
    choice = input("Введите команду: ")
    if choice == '?':
        print("\nВведите 'p' для определения кому принадлежит документ. "
              "\nВведите 'l' для вывода списка документов"
              "\nВведите 's' для определения на какой полке находится документ."
              "\nВведите 'a', чтобы добавить новый документ.")
    elif choice == 'p':
        people()
    elif choice == 'l':
        list()
    elif choice == 's':
        shelf()
    elif choice == 'a':
        add()