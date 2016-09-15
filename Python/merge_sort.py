import random
import time

start_time = time.time()

def merge_sort(array):
    if len(array) > 1:
        m = len(array)//2
        left = array[:m]
        right = array[m:]
        merge_sort(left)
        merge_sort(right)
        merge(array, left, right)

def merge(array, leftArray, rightArray):
    i = 0
    l_i = 0
    r_i = 0
    while l_i < len(leftArray) and r_i < len(rightArray):
        if leftArray[l_i] < rightArray[r_i]:
            array[i] = leftArray[l_i]
            l_i += 1
        else:
            array[i] = rightArray[r_i]
            r_i += 1
        i += 1
    # copy the remaining
    while l_i < len(leftArray):
        array[i] = leftArray[l_i]
        l_i += 1
        i += 1
    while r_i < len(rightArray):
        array[i] = rightArray[r_i]
        r_i += 1
        i += 1

a = [random.randint(0, 1000000) for i in range(0,1000000)]
# print(a)
# merge_sort(a)
a.sort()
# a.sort()
# print(a)
print("--- %s seconds ---" % (time.time() - start_time))
