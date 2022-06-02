
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
    while i < len(list1):
        res.append(list1[i])
        i += 1
    while j < len(list2):
        res.append(list2[j])
        j += 1
    return res

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))
print(merge_sort([3, 1, 4, 2, 5,6]))