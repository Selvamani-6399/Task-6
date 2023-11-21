# Python program to print Odd and Even Numbers in a List
list1 = [10,501,22,37,100,999,87,351]

even = []
odd = []

for num in list1:
    if(num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)
        
print("Even List: ",even)
print("Odd List: ",odd)