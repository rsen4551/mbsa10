#  display prime numbers from 3 to 30
for num in range(3,31):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            break;
        else:
            print(num, " it is prime")
            break;