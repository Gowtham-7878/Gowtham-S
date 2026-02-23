def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(6))


def fact(n):
    if n==0 or n==1:
        return 1
    return  fact(n**2)
print(fact(6))