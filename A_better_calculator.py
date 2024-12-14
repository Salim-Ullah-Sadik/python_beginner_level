num1 =float(input("Enter First Number : "))
op=input("Enter Operation : ")
num2=float(input("Enter Second Number :"))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("Invalid Operation")

