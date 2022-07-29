# check Fibonacci
fibo =[0,1]
[fibo.append(fibo[-2]+fibo[-1]) for i in range(5)]
fibo
print(fibo)


# Palindrome
text = 'level'
ispalindrome = text == text[::-1]
print(ispalindrome)

#Transpose
a=[[1,2,3,4],[5,6,7,8],[9,0,1,9]]
tranpose=[list(i) for i in zip(*a)]
print(tranpose)


# list
lst = list(range(0,99))
print(lst)

# type casting
it = list(map(int,['1','3','2']))
print(it)
ft = list(map(float,it))
print(ft)
ftg = [float(i) for i in it]
print(ftg)