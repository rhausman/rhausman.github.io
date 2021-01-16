def my_sort(lst):
    # base case - singleton or empty list
    if len(lst) <= 1:
        return lst
    # recursive case: sort each half, then merge
    else:
        return merge(my_sort(lst[::2]), my_sort(lst[1::2]))


def merge(ls1, ls2):
    # merge 2 pre-sorted lists
    if ls1 == []:
        return ls2
    elif ls2 == []:
        return ls1
    elif ls1[0] < ls2[0]:
        return [ls1[0]] + merge(ls1[1:], ls2)
    else:
        return [ls2[0]] + merge(ls1, ls2[1:])
