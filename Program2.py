# Count all the prime numbers

l=[10,501,22,37,100,999,87,351]
prime=[]
for i in l:
    c=0
    for j in range(1,i):
        if i % j == 0:
            c=c+1
    if c == 1:
        prime.append(i)
print("prime number is:", prime)   