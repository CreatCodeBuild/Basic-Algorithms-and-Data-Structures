# last element pivot

import random
import time

start_time = time.time()
# end is included index
def quick_sort(array, start, end):
    # global step
    # if step < 10:
    #     step += 1
    # else:
    #     return
    # print('s', array, start, end)
    if end > start:
        wall = partition(array, start, end)
        quick_sort(array, start, wall-1)
        quick_sort(array, wall+1, end)

# pivot is the end
def partition(array, start, end):
    # global step
    # if step < 10:
    #     step += 1
    # else:
    #     return
    # print('p', array, start, end)
    cur = start
    wall = start
    for cur in range(start, end):
        if array[cur] < array[end]:
            array[wall], array[cur] = array[cur], array[wall]
            wall += 1
    array[wall], array[end] = array[end], array[wall]
    # print(wall)
    return wall

# a = [4, 2, 5, 9, 7]
# quick_sort(a, 0, len(a)-1)
# print(a)

a = [random.randint(0, 1000000) for i in range(0,1000000)]
# print(a)
# merge_sort(a)
quick_sort(a, 0, len(a)-1)
print("--- %s seconds ---" % (time.time() - start_time))
