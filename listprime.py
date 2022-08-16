import math

n = int(input("Please enter a whole number: "))

def prime_numbers(n):
    if (n!=0):
        while (n%2 == 0):
            print(int(2)),
            n = n/2
            break
        for i in range(3, int(math.sqrt(n))+1, 2):
            while (n%i == 0):
                print(int(i)),
                n = n/i
                break
        if (n>2):
            print(int(n))
    else:
        print("0")

prime_numbers(n)