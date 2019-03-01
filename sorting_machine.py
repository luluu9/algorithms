from random import randint


def generate_lst(length):
    lst = []
    for i in range(length):
        lst.append(randint(0, 100000))
    return lst


def bubble_sorting(lst):
    moved = True
    while moved is True:
        moved = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                moved = True
    return lst


lst = generate_lst(10)
print(bubble_sorting(lst))
