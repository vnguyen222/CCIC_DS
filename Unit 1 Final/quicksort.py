########################
# GENERATION OF LIST
########################

from random import randint

def GENERATE_LIST(length, range_bounds = [0, 100000]):
    list = []
    for x in range(length):
        list.append(randint(range_bounds[0], range_bounds[1]))
    return list


########################
# QUICK SORT
########################

unsorted_list = [1,64,32,3,4,5,10,34,65,7,8]

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

    return lower_index+1


# TESTING
from time import time

# 10, 50, 1000, 50000, 1500000
def time_trials(list_of_len):
    times = []
    for x in list_of_len:
        list = GENERATE_LIST(x)
        print("Generated list of", x)
        start = time()
        quicksort(list, 0, len(list)-1)
        end = time()
        print("List of", x, "elements sorted.")
        delta = end - start
        times.append([x, delta])
        print("Done in", delta, "seconds \n\n")
    return times

runs = time_trials([2, 10, 50, 1000, 50000, 100000, 135325, 250000, 500000, 750000, 1000000, 1500000, 2000000, 5000000, 10000000, 20000000])
print(runs)