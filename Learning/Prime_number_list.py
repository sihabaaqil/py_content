import sys

# num = 12
num1 = [111, 2, 3, 4, 5, 7, 8, 9]
print(num1) #37
print(sys.getsizeof(num1))   #64    #120
print(num1.__sizeof__())    #48     #104
print(len(num1))            #1       #8
# Using for loop
for i in num1:
    # print(i)//test
    flag = False
    # prime numbers are greater than 1
    if i > 1:
        # check for factors
        for i in range(2, i):
            if (i % i) == 0:
                # if factor is found, set flag to True
                flag = True
                break
    if flag:
        print(i, "is not a prime number")
    else:
        print(i, "is a prime number")
