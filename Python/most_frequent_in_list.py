def most_frequent(list):
    return max(set(list), key=list.count)

mylist = [1,1,2,3,4,5,5,1,2,1,]
print("Item withthe most frequency: ", most_frequent(mylist)) 