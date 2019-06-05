# TO-DO: complete the help function below to merge 2 sorted arrays
a=[3,6,9]
b=[2,4,8]
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    i = j = 0
    while (i < len(arrA) and j < len(arrB)):
        if arrA[i] >= arrB[j]:
            merged_arr.append(arrB[j])
            j+=1
        else:
            merged_arr.append(arrA[i])
            i+=1
    merged_arr += arrA[i:]
    merged_arr += arrB[j:]

    return merged_arr
    
print(merge(a, b))

# TO-DO: implement the Merge Sort function below USING RECURSION
array = [2, 1, 4, 53, 62, 7, 12, 9]
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    cut = int(len(arr)/2)
    start = merge_sort(arr[:cut])
    end = merge_sort(arr[cut:])
    newArr = merge(start, end)
    return newArr

print(merge_sort(array))



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr




# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
