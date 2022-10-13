########################
# QUICK SORT
########################

def quicksort(list, start, end):
    if start < end:
        partition_index = partition(list, start, end)
        quicksort(list, start, partition_index - 1)
        quicksort(list, partition_index+1, end)
    
    return list

def partition(list_p, start, end):
    pivot = list_p[end]
    lower_index = start-1
    for x in range(start, end):
        if (list_p[x] < pivot):
            lower_index += 1
            
            # Swap
            temp = list_p[lower_index]
            list_p[lower_index] = list_p[x]
            list_p[x] = temp
    
    # Swap
    temp = list_p[lower_index+1]
    list_p[lower_index+1] = list_p[end]
    list_p[end] = temp

    # print("Pivot: ", pivot)
    # print(list_p)

    return lower_index+1


if __name__ == "__main__":
    unsorted_list = [1,64,32,3,4,5,10,34,65,7,8]
    print("Sorted:", quicksort(unsorted_list, 0, len(unsorted_list)-1))