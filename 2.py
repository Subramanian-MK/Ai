import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
def binary_search(n, a, k, low, high):
    mid = int((low + high) / 2)
    if low > high:
        return -1
    if k == a[mid]:
        return mid
    elif k < a[mid]:
        return binary_search(n, a, k, low, mid - 1)
    else:
        return binary_search(n, a, k, mid + 1, high)
x = []
y = []
for i in range(5):
    n = int(input("\nEnter the value of n: "))
    x.append(n)
    arr = [x for x in range(n)]
    k = random.randint(0, n)
    start = timer()
    ind = binary_search(n, arr, k, 0, n - 1)
    end = timer()
    y.append(end - start)
    print("Array elements are in the range of 0 -", n)
    print("k value =", k)
    print("Time taken =", end - start)
    print("Element is at the index:", ind)
plt.plot(x, y)
plt.title('Time Taken for Binary Search')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.show()
