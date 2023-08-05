a = int(input("Enter first number :"))
b = int(input("Enter second number : "))
c = input("Enter Operator : a) +\nb) -\nc) *\nd) /\ne) %\n")
if(c=='+'):
    print("The result is : ", a+b)
elif(c=='-'):
    print("The result is : ",a-b)
elif(c=='*'):
    print("The result is : ",a*b)
elif(c=='/'):
    print("The result is : ",a/b)
elif(c=='%'):
    print("The result is : ",a%b)
else:
    print("Error ! Invalid Input !")