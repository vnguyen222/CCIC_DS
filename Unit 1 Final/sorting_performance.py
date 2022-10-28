from sys import setrecursionlimit
setrecursionlimit(1000000000)

from quicksort import quicksort

########################
# GENERATION OF LIST
########################

from random import randint

def GENERATE_LIST(length):
    list = []
    range_bounds = [-1000000, 1000000]
    for x in range(length):
        list.append(randint(range_bounds[0], range_bounds[1]))
    return list



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
def sort_mem(list):
    tracemalloc.start() # START MEMORY TRACKING
    x1, y1 = tracemalloc.get_traced_memory()
    quicksort(list, 0, len(list)-1)
    x2, y2 = tracemalloc.get_traced_memory()
    tracemalloc.stop()  # START MEMORY TRACKING
    print("List of", len(list), "elements sorted.")
    peak_mem = y2 - y1
    print(peak_mem, "bytes used", end="\n\n")
    return peak_mem



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

    OPTION = 2
    # Fully RANDOM - TIME       1
    # FIRST HALF SORTED - TIME  2
    # SECOND HALF SORTED - TIME 3
    # Fully SORTED - TIME       4
    # Fully RANDOM - MEM        5
    # FIRST HALF SORTED - MEM   6
    # SECOND HALF SORTED - MEM  7
    # Fully SORTED - MEM        8



    if OPTION == 1:
        times = []

        print("////////////////////////////")
        print("STARTING FULLY RANDOM - TIME")
        print("////////////////////////////", end="\n")
        sleep(1)

        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            times.append(sort_time(list))

        print(times, end="\n\n")
        for x in range(0, len(times)):
            print(str(power_2[x]) + "\t\t" + str(times[x]))

    elif OPTION == 2:
        times = []

        print("/////////////////////////////////////////")
        print("STARTING FIRST HALF PARTIAL SORTED - TIME")
        print("/////////////////////////////////////////", end="\n")
        sleep(1)

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

    elif OPTION == 3:
        times = []

        print("//////////////////////////////////////////")
        print("STARTING SECOND HALF PARTIAL SORTED - TIME")
        print("//////////////////////////////////////////", end="\n")
        sleep(1)

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
            times.append(sort_time(list))
        
        print(times, end="\n\n")
        for x in range(0, len(times)):
            print(str(power_2[x]) + "\t\t" + str(times[x]))

    elif OPTION == 4:
        times = []

        print("////////////////////////////")
        print("STARTING FULLY SORTED - TIME")
        print("////////////////////////////", end="\n")
        sleep(1)

        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Sort list
            list.sort()
            print("Initially sorted second half")

            # Sorting
            times.append(sort_time(list))

        print(times, end="\n\n")
        for x in range(0, len(times)):
            print(str(power_2[x]) + "\t\t" + str(times[x]))


    elif OPTION == 5:
        mem_usage = []

        print("///////////////////////////")
        print("STARTING FULLY RANDOM - MEM")
        print("///////////////////////////", end="\n")
        sleep(1)

        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            mem_usage.append(sort_mem(list))

        print(mem_usage, end="\n\n")
        for x in range(0, len(mem_usage)):
            print(str(power_2[x]) + "\t\t" + str(mem_usage[x]))

    elif OPTION == 6:
        mem_usage = []

        print("/////////////////////////////////")
        print("STARTING PARTIALLY SORTED - MEM 1")
        print("/////////////////////////////////", end="\n")
        sleep(1)

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
            mem_usage.append(sort_mem(list))
        
        print(mem_usage, end="\n\n")
        for x in range(0, len(mem_usage)):
            print(str(power_2[x]) + "\t\t" + str(mem_usage[x]))

    elif OPTION == 7:
        mem_usage = []

        print("/////////////////////////////////")
        print("STARTING PARTIALLY SORTED - MEM 2")
        print("/////////////////////////////////", end="\n")
        sleep(1)

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
            mem_usage.append(sort_mem(list))
        
        print(mem_usage, end="\n\n")
        for x in range(0, len(mem_usage)):
            print(str(power_2[x]) + "\t\t" + str(mem_usage[x]))

    elif OPTION == 8:
        mem_usage = []

        print("///////////////////////////")
        print("STARTING FULLY SORTED - MEM")
        print("///////////////////////////", end="\n")
        sleep(1)

        for x in power_2:
            list = GENERATE_LIST(x)
            print("Generated list of", x)

            # Sort list
            list.sort()
            print("Initially sorted second half")

            # Sorting
            mem_usage.append(sort_time(list))

        print(mem_usage, end="\n\n")
        for x in range(0, len(mem_usage)):
            print(str(power_2[x]) + "\t\t" + str(mem_usage[x]))
