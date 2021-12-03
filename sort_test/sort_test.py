#!usr/bin/python3
"""
This file creates a script that generates a random list and then sorts the list using a bubble
sort, merge sort, and pythons built in list sort. The purpose of this is to use the cProfile
module to time the different sort functions. The results of the cProfile are included as comments
at the end of the file.
"""

import random


def bubble_sort(unsortlist):
    listlength = len(unsortlist)
    slist = unsortlist[:]
    for i in range(listlength):
        for k in range(listlength - (i + 1)):
            if slist[k] > slist[k+1]:
                slist[k], slist[k+1] = slist[k+1], slist[k]
    return slist


def merge_sort(unsortlist):
    if len(unsortlist) > 1:
        mid = int(len(unsortlist) / 2)
        left = merge_sort(unsortlist[:mid])
        right = merge_sort(unsortlist[mid:])
        templist = []
        ir, il, k = 0, 0, 0
        while k < len(unsortlist):
            if il >= len(left) and ir < len(right):
                templist.append(right[ir])
                ir += 1
            elif ir >= len(right) and il < len(left):
                templist.append(left[il])
                il += 1
            elif left[il] <= right[ir]:
                templist.append(left[il])
                il += 1
            elif right[ir] < left[il]:
                templist.append(right[ir])
                ir += 1
            k += 1
        # print(templist[0])
        return templist
    return unsortlist


if __name__ == "__main__":
    randlist = [random.randint(0, 100000000) for i in range(1000)]
    # print(randlist)
    merge_list = merge_sort(randlist)
    randlist.sort()
    bubble_list = bubble_sort(randlist)
    # print(merge_list)
    # print(bubble_list)
    # print(randlist)

"""
Thu Nov  7 18:05:54 2019    hw9_results

         53987 function calls (51944 primitive calls) in 0.173 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.139    0.139    0.139    0.139 hw9.py:6(bubble_sort)
   1999/1    0.011    0.000    0.015    0.015 hw9.py:16(merge_sort)
        6    0.006    0.001    0.006    0.001 {built-in method _imp.create_dynamic}
        3    0.006    0.002    0.006    0.002 {built-in method builtins.compile}
    34565    0.003    0.000    0.003    0.000 {built-in method builtins.len}
     1000    0.001    0.000    0.003    0.000 /opt/python/lib/python3.6/random.py:172(randrange)
     9976    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
     1000    0.001    0.000    0.001    0.000 /opt/python/lib/python3.6/random.py:222(_randbelow)
       51    0.001    0.000    0.001    0.000 {built-in method posix.stat}
     1000    0.001    0.000    0.003    0.000 /opt/python/lib/python3.6/random.py:216(randint)
       33    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:1233(find_spec)
        1    0.000    0.000    0.004    0.004 hw9.py:42(<listcomp>)
     1322    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
      144    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:57(_path_join)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:830(get_data)
      144    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:59(<listcomp>)
        3    0.000    0.000    0.000    0.000 {built-in method marshal.dumps}
       18    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
      294    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        9    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:861(_find_spec)
        1    0.000    0.000    0.011    0.011 /opt/python/lib/python3.6/random.py:38(<module>)
        9    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:1117(_get_spec)
      168    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:208(_verbose_message)
"""