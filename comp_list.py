# def compare_list():
#     list1 = [1, 5, 10, 12, 16, 20]
#     list2 = [1, 2, 10, 13, 16]
#     lis = list1+list2
#     i=0
#     empty_lis=[ ]
#     while i <len(lis):
#         if lis[i] not in empty_lis:
#             empty_lis.append(lis[i])
#             value = sorted(empty_lis)
#         i+=1
#     return value
# print(compare_list())

string="i am sandhya"
string1=" "
new=[]
for i in string:
    if i==",":
        new.append(string1)
        string1=","
    else:
        string1=string1+i
else:
    new.append(string1)
print(new)