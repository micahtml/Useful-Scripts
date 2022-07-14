def merge_2_dict(dict1, dict2):
    d = dict1.copy() # use the copy method
    d.update(dict2) # use the update method
    return d # return without changing the original dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_2_dict(dict1, dict2) # merge dictionaries

print(merged_dict)