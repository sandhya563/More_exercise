def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"is max number")
    if num2>num1 and num2>num3:
        print(num2,"is max number")
    if num3>num1 and num3>num2:
        print(num3,"is max number")
num1=int(input("enter number="))
num2=int(input("enter number="))
num3=int(input("enter number="))
max(num1,num2,num3)
