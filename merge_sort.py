
def merge(list1, list2):
    res = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    while i < len(list2):
        res.append(list1[i])
        i += 1
    while j < len(list2):
        res.append(list2[j])
        j += 1
    return res

list3 = [1, 3, 8, 11]
list4 = [2, 4, 5, 10]
print(merge(list3, list4))