def atm(number):
   l = len(number)
   b = ('*' * (l-4)) + ( number[-4:])
   return b 


atm_number = input("Enter your atm number:")  
print (atm(atm_number))
