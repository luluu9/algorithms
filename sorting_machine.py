from random import randint


def generate_lst(length):
    lst = []
    for i in range(length):
        lst.append(randint(0, 1000))
    return lst


def bubble_sorting(lst):
    moved = True
    while moved is True:
        moved = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                moved = True
    return lst


def selection_sorting(lst):
    d = len(lst)
    for i in range(d):
        smallest = lst[i]
        smallestIndex = i
        for j in range(i + 1, d):
            if (lst[j] < smallest):
                smallest = lst[j]
                smallestIndex = j
        buff = lst[i]
        lst[i] = smallest
        lst[smallestIndex] = buff
    return lst


def merge_sorting(lst):
    def merge(left_lst, right_lst):
        lst = []
        final_len = len(left_lst) + len(right_lst)
        while(len(lst) < final_len):
            if not left_lst:
                lst += right_lst
                break
            if not right_lst:
                lst += left_lst
                break
            #########
            if left_lst[0] < right_lst[0]:
                lst.append(left_lst.pop(0))
            elif right_lst[0] < left_lst[0]:
                lst.append(right_lst.pop(0))
            else:
                lst.append(left_lst.pop(0))
        return lst

    if len(lst) < 2:
        return lst
    else:
        left_lst = lst[:len(lst) // 2]
        right_lst = lst[len(lst) // 2:]
        left_lst_sorted = merge_sorting(left_lst)
        right_lst_sorted = merge_sorting(right_lst)
        lst = merge(left_lst_sorted, right_lst_sorted)
        return lst


lst = generate_lst(30)
print(selection_sorting(lst))
print(bubble_sorting(lst))
print(merge_sorting(lst))
