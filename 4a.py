import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
x = []
y = []
for i in range(3):
    n = int(input("\nenter the value of n:"))
    x.append(n)
    arr = [random.randint(0, 1000) for _ in range(n)]
    print("\nthe array elements are",arr)
    start_time = timer()
    insertionSort(arr)
    end_time = timer()
    print("array elements are ", arr)
    elapsed_time = end_time - start_time
    y.append(elapsed_time)
    print("time taken=", elapsed_time)
plt.plot(x, y)
plt.title('Time Taken for insertion sort')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.show()
