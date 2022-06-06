def function(a,op,c):
  
    if (op == '+'):
       return(a+c)
    if (op == '-'):
       return(a-c) 
    if (op == '/'):
       return(a/c)  
    if (op == '*'):
       return(a*c)

num1 = int(input("enter the number1:"))  
num2 = int(input("enter the number2:"))   
operation = input("write the operation:")  
result = function(num1,operation,num2)   
print(result)   

         
