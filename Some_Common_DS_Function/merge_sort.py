# Recursively implementation of Merge Sort
number = 0
def merge(left, right):
    result = []
    global number
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
            #count += len(right)
        else:
            result.append(right.pop(0))
            number += len(left)
    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(L):
    if len(L) <= 1:
        # When D&C to 1 element, just return it
        return L
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
    # return the answer of sub-problem
if __name__ == "__main__":
    test = [5,2,6,1,3]
    print("original:", test)
    print("Sorted:", merge_sort(test))
    print("Inversion Pairs numbers:",number)