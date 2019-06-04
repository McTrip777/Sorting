# TO-DO: Complete the selection_sort() function below 
arr = [643,44,32,1,25,56,73,8,34,69,23,67]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        # smallest_index = current_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[current_index]:
                current_index = j
            
        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[current_index]
        arr[current_index] = temp

    return arr

# print(selection_sort(arr))
    # temp = i
    # i = j
    # j = temp

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):  
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr
# arr = [643,44,32,1,25,56,73,8,34,69,23,67]

print(bubble_sort(arr))




# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr