def swap(my_list, idx1, idx2):
    my_list[idx1], my_list[idx2] = my_list[idx2], my_list[idx1]
    #function：换位置，swap

def pivot(my_list, p_idx, end_idx):
    #三个指针
    #i 逐个往后比较
    #初始化位置：swap的位置=指针位置
    swap_idx = p_idx
    for i in range(p_idx+1, end_idx+1):
        if my_list[i] < my_list[p_idx]:
            swap_idx += 1
            swap(my_list, swap_idx,i)
    swap(my_list, p_idx, swap_idx)
    return swap_idx
#time complexity: O(n), since we run though all arr here

def helper(my_list, left, right):
    if left < right:
        pivot_idx = pivot(my_list, left, right)
        helper(my_list, left, pivot_idx-1)
        helper(my_list, pivot_idx + 1, right)
    return my_list
#time complexity: O(log（n）) 因为这里每次我们把arr一分为二，每次二分， 所以就是log（n）
def quick_sort(my_list):
    return helper(my_list, 0, len(my_list)-1)
print(quick_sort([4, 5, 1, 3, 2]))
# time compleixty: O(n * log(n)) -> average case
# but if we have a sorted list, it will be O(n **2)