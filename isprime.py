n = int(input("Please enter a whole number: "))

if n > 1:
    if n == 2:
        print(n, "is a prime number")
    for i in range(2, int(n)):
        if (n%i == 0):
            print(n, "is not a prime number")
            break
        else:
            print(n, "is a prime number")
            break
else:
    print(n, "is not a prime number")
