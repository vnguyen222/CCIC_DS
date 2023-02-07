from re import T
from sys import setrecursionlimit
setrecursionlimit(1000000000)

from quicksort import quicksort

########################
# GENERATION OF LIST
########################

from random import randint
from random import uniform

def GENERATE_LIST(length):
    list = []
    range_bounds = [-1000000, 1000000]
    for x in range(length):
        list.append(randint(range_bounds[0], range_bounds[1]))
    return list
def generate_floats(length):
    list = []
    range_bounds = [-1000000, 1000000]
    for x in range(length):
        list.append(uniform(range_bounds[0], range_bounds[1]))
    return list
def generate_letters(length):
    list = []
    range_bounds = [97, 122]
    for x in range(length):
        list.append(randint(range_bounds[0], range_bounds[1]))
    return list

def clear_file():
    open("dump.txt", "w").close()
def append_to_file(content):
    with open("dump.txt", "a") as f:
        f.write(str(content) + "\n")

########################
# EXECUTION OF SORTING
########################
from time import time
from time import sleep
from math import pow
import tracemalloc


# TIME
def sort_time(list):
    start = time()
    quicksort(list, 0, len(list)-1)
    end = time()
    print("List of", len(list), "elements sorted.")
    delta = end - start
    print("Done in", delta, "seconds \n\n")
    return delta

# MEMORY
def sort_memory(list):
    tracemalloc.start() # START MEMORY TRACKING
    x1, y1 = tracemalloc.get_traced_memory()
    quicksort(list, 0, len(list)-1)
    x2, y2 = tracemalloc.get_traced_memory()
    tracemalloc.stop()  # START MEMORY TRACKING
    print("List of", len(list), "elements sorted.")
    peak_mem = y2 - y1
    print(peak_mem, "bytes used", end="\n\n")
    return peak_mem

# Number of Operations
number_of_operations = 0
def sort_operations(list):
    global number_of_operations
    number_of_operations = 0
    sort_operations_QUICKSORT(list, 0, len(list)-1)
    print("List of", len(list), "elements sorted.")
    print(number_of_operations, "performed", end="\n\n")
    return number_of_operations

def sort_operations_QUICKSORT(list, start, end):
    global number_of_operations
    if start < end:
        number_of_operations += 1
        partition_index = sort_operations_PARTITION(list, start, end)
        sort_operations_QUICKSORT(list, start, partition_index - 1)
        sort_operations_QUICKSORT(list, partition_index+1, end)
    return list
def sort_operations_PARTITION(list_p, start, end):
    global number_of_operations
    pivot = list_p[end]
    lower_index = start-1
    for x in range(start, end):
        if (list_p[x] < pivot):
            number_of_operations += 1
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


# Exponential growth of length
def exponential_list(max_value):
    list = []
    power = 1
    while True:
        list_len = pow(2, power)
        if list_len < max_value:
            list.append(int(list_len))
        else:
            break
        power += 1
    
    return list


if __name__ == "__main__":
    # personal_elements = [2, 10, 50, 1000, 50000, 100000, 135325, 250000, 500000, 750000, 1000000, 1500000, 2000000, 5000000, 10000000, 20000000]
    power_2 = exponential_list(1500000)

    OPTION = 4
    # Fully RANDOM - TIME       1
    # FIRST HALF SORTED - TIME  2
    # SECOND HALF SORTED - TIME 3
    # Fully SORTED - TIME       4
    # Fully RANDOM - MEM        5
    # FIRST HALF SORTED - MEM   6
    # SECOND HALF SORTED - MEM  7
    # Fully SORTED - MEM        8
    # Fully RANDOM - OPER       9
    # FIRST HALF SORTED - OPER  10
    # SECOND HALF SORTED - OPER 11
    # Fully SORTED - OPER       12



    if OPTION == 1:
        times = []

        print("////////////////////////////")
        print("STARTING FULLY RANDOM - TIME")
        print("////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = generate_letters(x)
            print("Generated list of", x)

            # Sorting
            t = sort_time(list)
            times.append(t)
            append_to_file(t)

        print(times, end="\n\n")
        for x in range(0, len(times)):
            print(str(power_2[x]) + "\t\t" + str(times[x]))

    elif OPTION == 2:
        times = []

        print("/////////////////////////////////////////")
        print("STARTING FIRST HALF PARTIAL SORTED - TIME")
        print("/////////////////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Split list and sort first half
            split = len(list) // 2
            split_first_half = list[:split]
            split_first_half.sort()
            print("Initially sorted first half")
            split_second_half = list[split:]
            list = split_first_half + split_second_half

            # Sorting
            times.append(sort_time(list))
        
        print(times, end="\n\n")
        for x in range(0, len(times)):
            print(str(power_2[x]) + "\t\t" + str(times[x]))
            append_to_file(times[x])

    elif OPTION == 3:
        times = []

        print("//////////////////////////////////////////")
        print("STARTING SECOND HALF PARTIAL SORTED - TIME")
        print("//////////////////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Split list and sort second half
            split = len(list) // 2
            split_first_half = list[:split]
            split_second_half = list[split:]
            split_second_half.sort()
            print("Initially sorted second half")
            list = split_first_half + split_second_half

            # Sorting
            t = sort_time(list)
            times.append(t)
            append_to_file(t)
        print(times, end="\n\n")
        for x in range(0, len(times)):
            print(str(power_2[x]) + "\t\t" + str(times[x]))

    elif OPTION == 4:
        times = []

        print("////////////////////////////")
        print("STARTING FULLY SORTED - TIME")
        print("////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Sort list
            list.sort()
            print("Initially sorted second half")

            # Sorting
            t = sort_time(list)
            times.append(t)
            append_to_file(t)

        print(times, end="\n\n")
        for x in range(0, len(times)):
            print(str(power_2[x]) + "\t\t" + str(times[x]))


    elif OPTION == 5:
        mem_usage = []

        print("///////////////////////////")
        print("STARTING FULLY RANDOM - MEM")
        print("///////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            mem_usage.append(sort_memory(list))

        print(mem_usage, end="\n\n")
        for x in range(0, len(mem_usage)):
            print(str(power_2[x]) + "\t\t" + str(mem_usage[x]))
            append_to_file(mem_usage[x])

    elif OPTION == 6:
        mem_usage = []

        print("/////////////////////////////////")
        print("STARTING PARTIALLY SORTED - MEM 1")
        print("/////////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Split list and sort first half
            split = len(list) // 2
            split_first_half = list[:split]
            split_first_half.sort()
            print("Initially sorted first half")
            split_second_half = list[split:]
            list = split_first_half + split_second_half

            # Sorting
            mem_usage.append(sort_memory(list))
        
        print(mem_usage, end="\n\n")
        for x in range(0, len(mem_usage)):
            print(str(power_2[x]) + "\t\t" + str(mem_usage[x]))
            append_to_file(mem_usage[x])

    elif OPTION == 7:
        mem_usage = []

        print("/////////////////////////////////")
        print("STARTING PARTIALLY SORTED - MEM 2")
        print("/////////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Split list and sort second half
            split = len(list) // 2
            split_first_half = list[:split]
            split_second_half = list[split:]
            split_second_half.sort()
            print("Initially sorted second half")
            list = split_first_half + split_second_half

            # Sorting
            m = sort_memory(list)
            mem_usage.append(m)
            append_to_file(m)

        
        print(mem_usage, end="\n\n")
        for x in range(0, len(mem_usage)):
            print(str(power_2[x]) + "\t\t" + str(mem_usage[x]))

    elif OPTION == 8:
        mem_usage = []

        print("///////////////////////////")
        print("STARTING FULLY SORTED - MEM")
        print("///////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Sort list
            list.sort()
            print("Initially sorted second half")

            # Sorting
            m = sort_memory(list)
            mem_usage.append(m)
            append_to_file(m)

        print(mem_usage, end="\n\n")
        for x in range(0, len(mem_usage)):
            print(str(power_2[x]) + "\t\t" + str(mem_usage[x]))


    elif OPTION == 9:
        oper_count = []

        print("////////////////////////////")
        print("STARTING FULLY RANDOM - OPER")
        print("////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Split list and sort first half
            split = len(list) // 2
            split_first_half = list[:split]
            split_first_half.sort()
            print("Initially sorted first half")
            split_second_half = list[split:]
            list = split_first_half + split_second_half

            oper_count.append(sort_operations(list))

        print(oper_count, end="\n\n")
        for x in range(0, len(oper_count)):
            print(str(power_2[x]) + "\t\t" + str(oper_count[x]))
            append_to_file(oper_count[x])

    elif OPTION == 10:
        oper_count = []

        print("/////////////////////////////////////////")
        print("STARTING FIRST HALF PARTIAL SORTED - OPER")
        print("/////////////////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            oper_count.append(sort_operations(list))

        print(oper_count, end="\n\n")
        for x in range(0, len(oper_count)):
            print(str(power_2[x]) + "\t\t" + str(oper_count[x]))
            append_to_file(oper_count[x])
    
    elif OPTION == 11:
        oper_count = []

        print("//////////////////////////////////////////")
        print("STARTING SECOND HALF PARTIAL SORTED - OPER")
        print("//////////////////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Split list and sort second half
            split = len(list) // 2
            split_first_half = list[:split]
            split_second_half = list[split:]
            split_second_half.sort()
            print("Initially sorted second half")
            list = split_first_half + split_second_half

            # Sorting
            o = sort_operations(list)
            oper_count.append(o)
            append_to_file(o)

        print(oper_count, end="\n\n")
        for x in range(0, len(oper_count)):
            print(str(power_2[x]) + "\t\t" + str(oper_count[x]))
    
    elif OPTION == 12:
        oper_count = []

        print("//////////////////////////////////////////")
        print("STARTING FULLY SORTED - MEM")
        print("//////////////////////////////////////////", end="\n")
        sleep(1)

        clear_file()
        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Sort list
            list.sort()
            print("Initially sorted second half")

            o = sort_operations(list)
            oper_count.append(o)
            append_to_file(o)

        print(oper_count, end="\n\n")
        for x in range(0, len(oper_count)):
            print(str(power_2[x]) + "\t\t" + str(oper_count[x]))
            append_to_file(oper_count[x])