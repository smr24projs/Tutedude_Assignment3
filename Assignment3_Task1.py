def factorial(n):
    if n==1:
        return 1
    else:
        global fact
        fact = n * factorial(n-1)
        return fact


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    fact = factorial(number)
    print(f"Factorial of {number} is: {fact}")
