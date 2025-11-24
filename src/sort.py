def bubble_sort(sp):
    flag = True
    while flag:
        flag = False
        for i in range(len(sp) - 1):
            if sp[i] > sp[i+1]:
                sp[i],sp[i+1] = sp[i+1],sp[i]
                flag = True
    return sp

sp = [1,0,2,5,7,1,2]
print(bubble_sort(sp))

def quick_sort(sp):
    if len(sp) <= 1:
        return sp
    pivot = sp[-1]
    left_pivot = [x for x in sp if x < pivot]
    middle_pivot = [x for x in sp if x == pivot]
    right_pivot = [x for x in sp if x > pivot]
    return quick_sort(left_pivot) + middle_pivot + quick_sort(right_pivot)

sp = [1,0,2,5,7,1,2]
print(quick_sort(sp))
