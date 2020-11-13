def list_function():
    list1 = [1, 342, 75, 23, 98,80,500,21]
    list2 = [75, 23, 98, 12, 78, 10, 1,80,500,21,100]
    empty=[]
    i=0
    while i<len(list1):
        j=0
        while j<len(list2):
            if list1[i] == list2[j]:
                b=list2[j]
                empty.append(b)
            j=j+1
        i=i+1
    return empty
print(list_function())