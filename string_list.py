def string_function():   
    string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
    empty_list=[]
    i=0
    while i<len(string_list):
        if string_list[i]not in empty_list:
            empty_list.append(string_list[i])
        i=i+1
    return empty_list
print(string_function())