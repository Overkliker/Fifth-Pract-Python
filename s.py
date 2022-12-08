import csv
from tabulate import tabulate


def plain_load(weight):
    """
    Функция загружает самолёт товаром одного типа на максимальную цену
    :param weight: станавливает занчение грузоподъёмности самолёта
    :return:
    """
    "Открытие csv файла с данными товаров"
    with open("plain.csv", 'r', encoding="windows-1251") as r:
        data = csv.reader(r)

        dict_of_products = {}
        for i in data:
            if i[1] in dict_of_products.keys():
                dict_of_products[i[1]] += [i]

            else:
                dict_of_products[i[1]] = [i]
        "Вывод всех типов товаров"
        ind = 1
        for i in dict_of_products.keys():
            print(f"{ind}. {i}")
            ind += 1
        name_prod = input("Введите тип товара: ")

        list_prod = [i for i in dict_of_products[name_prod]]

        "Выборка товаров для загрузки в самолёт"
        mass = 0
        col = 0
        list_with_products_on_plain = []
        for i in list_prod:
            if mass + float(i[4]) <= float(weight):
                for j in range(int(i[2])):
                    if mass + float(i[4]) > float(weight):
                        break

                    else:
                        mass += float(i[4])
                        col += 1
                i.pop(2)
                i.insert(2, str(col))
                list_with_products_on_plain.append(i)
                col = 0

        list_with_products_on_plain = list(sorted(list_with_products_on_plain, key=lambda x: x[0] and x[3]))

        "Вывод товаров погруженных в самолёт"
        head = ['Model', 'Class', 'Count', 'Price', 'Weight']
        print(tabulate(list_with_products_on_plain, headers=head))


plain_load(4)
