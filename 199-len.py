# Return the length (the number of items) of an object. 
# The argument may be a sequence (such as a string, tuple, list, or range) or a collection (such as a dictionary, set)

len('awesome') # 7
len((1,2,3,4)) # 4
len([1,2,3,4]) # 4
len(range(0,10)) # 10

len({1,2,3,4}) # 4
len({'a':1, 'b':2, 'c':2}) # 3
    
## exampler

class SpecialList:
 
    def __init__(self, data):
        self.__data = data
 
    def __len__(self):  # JUST LOOK AT THIS LINE
        return 50


l1 = SpecialList([1,40,30,100,30,1,2,3,4])
l2 = SpecialList([1,3,4,5]) 

print(len(l1)) #50
print(len(l2)) #50


