arr = []
for i in range (1,100):
    arr.append(i)
import random
n = random.randint(1,100)
arr.append(n)
print("the list of given numbers is :", arr)
for j in range (0,100):
    for k in  range (j+1,100):  
            if (arr[j]==arr[k]):
                print("the duplicate number is:", arr[j])

