def student_expenses(student,amaunt):
    multipul=student*amaunt
    print(multipul)
    if multipul < 50000:
        print("we are under tha budget")
    else:
        print("out of budget")
student=int(input("enter student ="))
amaunt=int(input("enter any amaunt ="))
student_expenses(student,amaunt)
