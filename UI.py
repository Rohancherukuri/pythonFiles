# Union and Intersection of two sorted arrays
from numpy import array

def union(arr1,arr2):
    size1,size2 = len(arr1),len(arr2)
    i = j = 0
    union_list = []
    while i < size1 and j < size2:
        if arr1[i] < arr2[j]:
            union_list.append(arr1[i])
            i += 1

        elif arr2[j] < arr1[i]:
            union_list.append(arr2[j])
            j += 1

        else:
            union_list.append(arr2[j])
            j += 1
            i += 1
    # Appending remaining elements of arrays
    while i < size1:
        union_list.append(arr1[i])
        i += 1

    while j < size2:
        union_list.append(arr2[j])
        j += 1
    return union_list

def intersection(arr1,arr2):
    size1,size2 = len(arr1),len(arr2)
    i = j = 0
    intersection_list = []
    while i < size1 and j < size2:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1

        else:
            intersection_list.append(arr2[j])
            j += 1
    return intersection_list
            

def main():
    # It only works for sorted arrays and without duplicates
    arr1 = array([1,3,4,5,6])
    arr2 = array([2,3,5,7])
    new_arr = union(arr1,arr2)
    print(repr(new_arr))
    new_arr2 = intersection(arr1,arr2)
    print(repr(new_arr2))
main()
