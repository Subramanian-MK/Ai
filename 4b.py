import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
x=[]
y=[]
for i in range(3):
    n=int(input("\nEnter the value of n:"))
    x.append(n)
    arr = [random.randint(0, 10) for _ in range(n)]
    print("Array elements before sorting are",arr)
    start_time = timer()
    sorted_arr = heapSort(arr)
    end_time = timer()
    elapsed_time = end_time - start_time
    y.append(elapsed_time)
    print("Array elements after sorting are ",sorted_arr)
    print("Time taken=", elapsed_time)
plt.plot(x,y)
plt.title('Time Taken for heap sort')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.show()
