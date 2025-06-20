num = int(input("Enter a number:"))

def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i

    return fac

print("Factorial of", num, "is:", factorial(num))