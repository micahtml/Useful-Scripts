def merge_2_dict(dict1, dict2):
    return(dict1.update(dict2)) # dict1 gets changed

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merge_2_dict(dict1, dict2 ) # merge these 2 dictionaries

print(dict2) # dict is changed and new dict is created

