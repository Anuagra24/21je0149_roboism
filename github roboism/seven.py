test_list = [6, 7, 3, 7, 7, 7, 6, 3, 7]
  
# printing original list
print ("Original list : " +str(test_list))
max = 0
res = test_list[0]
for i in test_list:
    
    freq = test_list.count(i)
    print(freq)
    if freq > max:
        max = freq
        res = i
print ("Most frequent number is : " + str(res))