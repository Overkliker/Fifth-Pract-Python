import csv
from tabulate import tabulate


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


parse_pers()