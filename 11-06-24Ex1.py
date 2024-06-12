#  display fibonicii series of 10 numbers
num=int(input("Enter the number of fibonicii series"))
a=0
b=1
c=0
print(a)
print(b)
i=1
while(i<num):
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)