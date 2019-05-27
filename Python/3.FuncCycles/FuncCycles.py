# Словарь students_dict, в нем уникальные ключи - student_id,
# значения - словари, ключи в словарях:
# имя (first_name), фамилия (last_name), пол (gender),
# предыдущий опыт в прог-нии (prog_exp)(True/False),
# ДЗ (homework_grades) (значение - список:
# не менее 5 оцененных ДЗ по 10-бальной шкале),
# экзамен (exam_grade) (оценка за экзамен по
# 10-балльной шкале).

# Для теста вывода интегральных оценок: у Петрова
# Василия и Липовой Дарьи одинаковые оценки.


import csv


def import_data():
    with open('students.csv', newline='', encoding='UTF-8') as csvfile:
        students_csv = csv.reader(csvfile, delimiter=';')
        import_list = list(students_csv)
    
    students_dict = dict()
    
    for i, student in enumerate(import_list):
        if i == 0:
            continue
        student_description = dict()
        for characteristic, value in zip(import_list[0], student):
            if characteristic == 'homework_grades':
                grades_list = list(value.split(","))
                int_grades_list = list(map(int, grades_list))
                student_description[characteristic] = int_grades_list
            elif characteristic == 'exam_grade':
                student_description[characteristic] = int(value)
            elif characteristic == 'id':
                student_id = int(value)
            else:
                student_description[characteristic] = value
        students_dict[student_id] = student_description
    return students_dict


def average_grade(students_dict, gender, exp, report_type):
    avg_grade_group = list()
    condition_1 = "student_description['gender'] in gender"
    condition_2 = "student_description['prog_exp'] in exp"
    for student_description in students_dict.values():
        if report_type == 'homework':
            if eval(condition_1) and eval(condition_2):
                grades = student_description['homework_grades']
                avg_grade_student = sum(grades) / len(grades)
                avg_grade_group.append(avg_grade_student)
        elif report_type == 'exam':
            if eval(condition_1) and eval(condition_2):
                avg_grade_group.append(student_description['exam_grade'])
        else:
            print("Неверный тип отчета.")
    avg_grade = sum(avg_grade_group) / len(avg_grade_group)
    return round(avg_grade, 3)


def best_students(students_dict):
    integral_grade_group = dict()
    best_students_names = dict()
    
    for student_id, student_description in students_dict.items():
        student_intgrl_grade = dict()
        name = student_description['last_name'] + ' ' + \
               student_description['first_name']
        integral_grade = (sum(student_description['homework_grades']) /
                          len(student_description['homework_grades'])) * 0.6 + (
                                 student_description['exam_grade'] * 0.4)
        student_intgrl_grade[name] = round(integral_grade, 3)
        integral_grade_group[student_id] = student_intgrl_grade

    intgrl_grade_info = list(integral_grade_group.values())
    student_max_grade = max(list(intgrl_grade_info[x].values())[0] for
                            x in range(len(intgrl_grade_info)))
    
    for student_id, intgrl_grade_info in integral_grade_group.items():
        for student_name, intgrl_grade in intgrl_grade_info.items():
            if intgrl_grade == student_max_grade:
                best_students_names[student_id] = student_name
    
    best_students_names['integral_grade'] = student_max_grade
    return (best_students_names)


def report_output():
    students_dict = import_data()
    
    print("Средняя оценка за домашние задания по группе:",
          average_grade(students_dict,
                        ['male', 'female'], ['True', 'False'], 'homework'))
    print("Средняя оценка за экзамен:",
          average_grade(students_dict,
                        ['male', 'female'], ['True', 'False'], 'exam'))
    
    print("\nСредняя оценка за домашние задания у мужчин:",
          average_grade(students_dict,
                        ['male'], ['True', 'False'], 'homework'))
    print("Средняя оценка за экзамен у мужчин:",
          average_grade(students_dict,
                        ['male'], ['True', 'False'], 'exam'))
    print("Средняя оценка за домашние задания у женщин:",
          average_grade(students_dict,
                        ['female'], ['True', 'False'], 'homework'))
    print("Средняя оценка за экзамен у женщин:",
          average_grade(students_dict,
                        ['female'], ['True', 'False'], 'exam'))
    
    print("\nСредняя оценка за домашние задания у "
          "студентов с опытом:",
          average_grade(students_dict,
                        ['male', 'female'], ['True'], 'homework'))
    print("Средняя оценка за экзамен у студентов с опытом:",
          average_grade(students_dict,
                        ['male', 'female'], ['True'], 'exam'))
    print("Средняя оценка за домашние задания у "
          "студентов без опыта:",
          average_grade(students_dict,
                        ['male', 'female'], ['False'], 'homework'))
    print("Средняя оценка за экзамен у студентов без опыта:",
          average_grade(students_dict,
                        ['male', 'female'], ['False'], 'exam'))
    
    student = best_students(students_dict)
    if len(list(student.keys())) == 2:
        amount_1 = 'й'
        amount_2 = ''
    elif len(list(student.keys())) > 2:
        amount_1 = 'е'
        amount_2 = 'ы'
    else:
        print("Ошибка во входных данных.")
    
    names = ''
    for key, value in student.items():
        if key != 'integral_grade':
            names += (value + ' (id: ' + str(key) + '), ')
    
    print("\n", "Лучши{} студент{}: {}с интегральной "
                "оценкой: {}".format(amount_1, amount_2, names,
                                     student['integral_grade']))


report_output()