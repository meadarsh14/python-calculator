print('''
+ add
- substract
* multiply
/ divide
''')

num1=int(input("enter the number 1"))
num2=int(input("enter the number 2"))
opr=input("enter the opr..")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print(invalid)