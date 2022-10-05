# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности в том же порядке.

# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

import random

def make_list(number_elem):
    list = [random.randint(0, 9) for i in range(0, number_elem)]

    return list


def make_result_list(list):
    list_ind_for_del = []
    i = 0
    while i < len(list):
        list_ind_for_del.append(i)
        flag_del = False
        for k in range(i + 1, len(list), 1):
            if list[i] == list[k]:
                list_ind_for_del.append(k)
                flag_del = True
        if flag_del:
            sdvig = 0
            for m in range(0, len(list_ind_for_del), 1):
                list.pop(list_ind_for_del[m] - sdvig)
                sdvig += 1
        else:
            i = i + 1
        list_ind_for_del.clear()

    return list


number_elem = int(input("Введите количество чисел ---> "))
if number_elem < 1:
    print("Input Error! Negative or zero value of the number of numbers!")
    exit()
list = make_list(number_elem)
print(f"Список чисел ---> {list}")
print(f"Список чисел без повторений ---> {make_result_list(list)}")
