user=int(input("enter any number"))
def is_hashad_number(user):
    num=user
    sum=0
    while user>0:
        stor=user%10
        sum=sum+stor
        user=user//10
    if num%sum==0:
        print("is hashad no")
    else:
        print("not hashad no")
is_hashad_number(user)

# num=int(input("enter your num"))
# store = num
# sum=0
# while num>0:
#     a=num%10
#     sum=sum+a
#     num=num//10
# if store%sum==0:
#     print("harshad")
# else:
#     print("not harshad")