def strohg_password(password):
    length=len(password)
    if length<=6 or length>=12:
        if "$" in password:
            if "2" in password or "8" in password:
                if password >= "A" and password <= "Z":
                    print("strong password")
                    
    else:
        print("week password")
password=input("enter any password= ")
strong_password(password)

# password=input("enter your password")
# length=len(password)
# for i in password:
#     if length>=6 or length<=12 and "$" in password and 2 in password and "Z" in password:
#         print(password,"strong password")
#         break
#     else:
#         print(password,"weak password")
#         break
