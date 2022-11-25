import random
a = random.randrange(0,10)
remainder = a%2
if (remainder == 0):
    print(a,"is a even number")
else:
    print(a,"is a odd number")

if (a>0):
    print(a,"is a positive number")
elif (a==0):
    print(a,"is a positive number")
else:
    print(a,"is a negative number")

for i in range (2,a):
    if a % i == 0:
        print(a,"is a composite number")
        break
else:
    print(a,"is a prime number")





