def bubble_sort(my_list):
    #[4, 2, 6, 5, 1, 3]
    #从index 5 开始， 到0， 每次从后往前移一步
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

print(bubble_sort([4, 6, 6, 5, 1, 1]))