import csv
from tabulate import tabulate


def csv_writer():
    """
    Функция добавляет ученика в файл
    :return:
    """
    name = input("Введите имя: ")
    school = input("Введите номер школы: ")
    f = input("Введите ответ на первый вопрос: ")
    s = input("Введите ответ на второй вопрос: ")
    fd = input("Введите ответ на третий вопрос: ")
    fr = input("Введите ответ на четвёртый вопрос: ")
    fi = input("Введите ответ на пятый вопрос: ")

    l1 = [name, school, f, s, fd, fr, fi]
    with open("fc.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",")
        file_writer.writerow(l1)

    print("Пользователь успешно добален")

def parse_pers():
    """
    Сортирует школьников по номеру школы и количеству выполненых задний.
    :return:
    """
    "Открытие файла с данными учеников"
    with open("fc.csv", 'r', encoding="windows-1251") as r:
        data = csv.reader(r)
        l1 = []
        d1 = {}
        for i in data:
            l1.append(i)

        for i in l1:
            if int(i[1]) not in d1.keys():
                d1[int(i[1])] = [i]

            else:
                d1[int(i[1])] = sorted(d1[int(i[1])] + [i], key=lambda x: x[1:].count('1'), reverse=True)
        "Вывод отсортированных учеников"
        head = ["Surname", 'School', '1', '2', '3', '4', '5']
        data = [i[1] for i in d1.items()]
        ""
        for i in data:
            print(tabulate(i, headers=head))
            print()


print("Что вы хотите сделать: вывести учеников - 1 или добавить участника - 2")
inp = int(input("Введите 1 или 2: "))
if inp == 1:
    parse_pers()

elif inp == 2:
    csv_writer()