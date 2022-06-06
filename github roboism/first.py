def func(array,str):
    if (str == "asce"):
     array.sort()
     return array
    elif (str == "desc"):
     array.sort(reverse=True)
     return array
    elif(str == "none"):
        return array


n = int(input("enter the number of elements in the list:"))
list=[]

for i in range(n):
    arr = int(input())

    list.append(arr)

string = input("enter the string:")

ans_list = func(list,string)

print(ans_list)