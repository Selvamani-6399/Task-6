# Python program to print duplicates from 
# a list of integers
list1 = [[1,2,4,6,8],[1,3,5,4,6],[1,2,4,6,8]]
dups = {tuple(x) for x in list1 
         if list1.count(x)>1}
print(dups)