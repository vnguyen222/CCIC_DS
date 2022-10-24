from sys import setrecursionlimit
setrecursionlimit(1000000)

from quicksort import quicksort

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
# EXECUTION OF SORTING
########################
# TESTING
from time import time
from time import sleep
from math import pow
import tracemalloc

def fully_random_time(list_of_len, random_range=[-1000000, 1000000]):
    times = []
    print("/////////////////////////////////")
    print("STARTING FULLY RANDOM - TIME")
    print("/////////////////////////////////", end="\n")
    sleep(1)
    for x in list_of_len:
        list = GENERATE_LIST(x, random_range)
        print("Generated list of", x)
        start = time()
        quicksort(list, 0, len(list)-1)
        end = time()
        print("List of", x, "elements sorted.")
        delta = end - start
        times.append([x, delta])
        print("Done in", delta, "seconds \n\n")
    return times

def half_sorted_time_1(list_of_len, random_range=[-1000000, 1000000]):
    times = []
    print("/////////////////////////////////")
    print("STARTING PARTIAL SORTED - TIME 1")
    print("/////////////////////////////////", end="\n")
    sleep(1)
    for x in list_of_len:
        list = GENERATE_LIST(x, random_range)
        print("Generated list of", x)

        split = len(list) // 2
        split_first_half = list[:split]
        split_first_half.sort()
        print("Initially sorted first half")
        split_second_half = list[split:]
        list = split_first_half + split_second_half

        start = time()
        quicksort(list, 0, len(list)-1)
        end = time()
        print("List of", x, "elements sorted.")
        delta = end - start
        times.append([x, delta])
        print("Done in", delta, "seconds \n\n")
    return times
def half_sorted_time_2(list_of_len, random_range=[-1000000, 1000000]):
    times = []
    print("/////////////////////////////////")
    print("STARTING PARTIAL SORTED - TIME 2")
    print("/////////////////////////////////", end="\n")
    sleep(1)
    for x in list_of_len:
        list = GENERATE_LIST(x, random_range)
        print("Generated list of", x)
        split = len(list) // 2
        split_first_half = list[:split]
        split_second_half = list[split:]
        split_second_half.sort()
        print("Initially sorted second half")
        list = split_first_half + split_second_half
        start = time()
        quicksort(list, 0, len(list)-1)
        end = time()
        print("List of", x, "elements sorted.")
        delta = end - start
        times.append([x, delta])
        print("Done in", delta, "seconds \n\n")
    return times

def fully_sorted_time(list_of_len, random_range=[-1000000, 1000000]):
    times = []
    print("/////////////////////////////////")
    print("STARTING FULLY SORTED - TIME")
    print("/////////////////////////////////", end="\n")
    sleep(1)
    for x in list_of_len:
        list = GENERATE_LIST(x, random_range)
        print("Generated list of", x)
        list.sort()
        print("Initially sorted")
        start = time()
        quicksort(list, 0, len(list)-1)
        end = time()
        print("List of", x, "elements sorted.")
        delta = end - start
        times.append([x, delta])
        print("Done in", delta, "seconds \n\n")
    return times


def fully_random_mem(list_of_len, random_range=[-1000000, 1000000]):
    mem_usage = []
    print("/////////////////////////////////")
    print("STARTING FULLY RANDOM - MEM")
    print("/////////////////////////////////", end="\n")
    sleep(1)
    for x in list_of_len:
        list = GENERATE_LIST(x, random_range)
        print("Generated list of", x)
        tracemalloc.start() # START MEMORY TRACKING
        x1, y1 = tracemalloc.get_traced_memory()
        quicksort(list, 0, len(list)-1)
        x2, y2 = tracemalloc.get_traced_memory()
        tracemalloc.stop()  # START MEMORY TRACKING
        print("List of", x, "elements sorted.")
        peak_mem = y2 - y1
        mem_usage.append([x, peak_mem])
        print(peak_mem, "bytes used", end="\n\n")
    return mem_usage

def half_sorted_mem_1(list_of_len, random_range=[-1000000, 1000000]):
    mem_usage = []
    print("/////////////////////////////////")
    print("STARTING PARTIALLY SORTED - MEM 1")
    print("/////////////////////////////////", end="\n")
    sleep(1)
    for x in list_of_len:
        list = GENERATE_LIST(x, random_range)
        print("Generated list of", x)

        split = len(list) // 2
        split_first_half = list[:split]
        split_first_half.sort()
        print("Initially sorted first half")
        split_second_half = list[split:]
        list = split_first_half + split_second_half

        print("Initially sorted")
        tracemalloc.start() # START MEMORY TRACKING
        x1, y1 = tracemalloc.get_traced_memory()
        quicksort(list, 0, len(list)-1)
        x2, y2 = tracemalloc.get_traced_memory()
        tracemalloc.stop()  # START MEMORY TRACKING
        print("List of", x, "elements sorted.")
        peak_mem = y2 - y1
        mem_usage.append([x, peak_mem])
        print(peak_mem, "bytes used", end="\n\n")
    return mem_usage
def half_sorted_mem_2(list_of_len, random_range=[-1000000, 1000000]):
    mem_usage = []
    print("/////////////////////////////////")
    print("STARTING PARTIALLY SORTED - MEM 2")
    print("/////////////////////////////////", end="\n")
    sleep(1)
    for x in list_of_len:
        list = GENERATE_LIST(x, random_range)
        print("Generated list of", x)
        
        split = len(list) // 2
        split_first_half = list[:split]
        split_second_half = list[split:]
        split_second_half.sort()
        print("Initially sorted second half")
        list = split_first_half + split_second_half

        print("Initially sorted")
        tracemalloc.start() # START MEMORY TRACKING
        x1, y1 = tracemalloc.get_traced_memory()
        quicksort(list, 0, len(list)-1)
        x2, y2 = tracemalloc.get_traced_memory()
        tracemalloc.stop()  # START MEMORY TRACKING
        print("List of", x, "elements sorted.")
        peak_mem = y2 - y1
        mem_usage.append([x, peak_mem])
        print(peak_mem, "bytes used", end="\n\n")
    return mem_usage


def fully_sorted_mem(list_of_len, random_range=[-1000000, 1000000]):
    mem_usage = []
    print("/////////////////////////////////")
    print("STARTING FULLY SORTED - TIME")
    print("/////////////////////////////////", end="\n")
    sleep(1)
    for x in list_of_len:
        list = GENERATE_LIST(x, random_range)
        print("Generated list of", x)
        list.sort()
        print("Initially sorted")
        tracemalloc.start() # START MEMORY TRACKING
        x1, y1 = tracemalloc.get_traced_memory()
        quicksort(list, 0, len(list)-1)
        x2, y2 = tracemalloc.get_traced_memory()
        tracemalloc.stop()  # START MEMORY TRACKING
        print("List of", x, "elements sorted.")
        peak_mem = y2 - y1
        mem_usage.append([x, peak_mem])
        print(peak_mem, "bytes used", end="\n\n")
    return mem_usage


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

    half1_runs_t = half_sorted_time_1(power_2)
    print(half1_runs_t, end="\n")
    for entry in half1_runs_t:
        for x in entry:
            print(float(x), end="\t\t")
        print()
    
    half2_runs_t = half_sorted_time_2(power_2)
    print(half2_runs_t, end="\n")
    for entry in half2_runs_t:
        for x in entry:
            print(float(x), end="\t\t")
        print()


    half1_runs_m = half_sorted_mem_1(power_2)
    print(half1_runs_m, end="\n")
    for entry in half1_runs_m:
        for x in entry:
            print(float(x), end="\t\t")
        print()
    
    half2_runs_m = half_sorted_mem_2(power_2)
    print(half2_runs_m, end="\n")
    for entry in half2_runs_m:
        for x in entry:
            print(float(x), end="\t\t")
        print()