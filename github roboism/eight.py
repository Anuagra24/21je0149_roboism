str = input("Enter the required string:")
n = len(str)
sum = 0
for i in range (0,n):
    if str[i].isdigit():
        p = int(str[i])
        sum = sum + p
print (sum)        