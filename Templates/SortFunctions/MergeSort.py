'''
归并排序，先分后并
'''
def merge_sort(arr):
    if len(arr) == 1:
        return arr 
    
    m = len(arr) // 2
    left = arr[:m]
    right = arr[m:]
    return merge_func(merge_sort(left),merge_sort(right))

def merge_func(l,r):
    # l,r是两个有序的数组，需要并在一起
    ptr1,ptr2 = 0,0
    res = []
    while ptr1 < len(l) and ptr2 < len(r):
        if l[ptr1] < r[ptr2]:
            res.append(l[ptr1])
            ptr1 += 1
        else:
            res.append(r[ptr2])
            ptr2 += 1
    res += l[ptr1:]
    res += r[ptr2:]
    return res 


if __name__ == "__main__":
    arr = [1,4,5,7,2,9,6]
    print(merge_sort(arr))