import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
x=[]
y=[]
for i in range(5):
    n=int(input("\nenter the value of n:"))
    x.append(n)
    arr = [random.randint(0, 1000) for _ in range(n)]
    k=random.randint(0,1000)
    start_time = timer()
    ind=linear_search(arr, k)
    end_time = timer()
    elapsed_time = end_time - start_time
    y.append(elapsed_time)
    print("array elements are in the range of 0-1000")
    print ("k value=",k)
    print("time taken=", elapsed_time)
    print ("element is at the index:",ind)
plt.plot(x,y)
plt.title('Time Taken for Linear Search')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.show()
