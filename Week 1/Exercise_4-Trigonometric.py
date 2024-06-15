import math
message = "n must be greater than 0"
def factorial(n):
    total = 1
    while n != 0:
        total = total * n
        n = n - 1
    return total

def approx_sin(x, n):
    if n <= 0:
        print(message)

    else:
        ans = 0
        for i in range(0, n):
            cal = ((-1) ** i) * ((x ** (2 * i + 1)) / factorial(2 * i + 1))
            ans += cal
        print(ans)

def approx_cos(x, n):
    if n <= 0:
        print(message)

    else:
        ans = 0
        for i in range(0, n):
            cal = ((-1) ** i) * ((x ** (2 * i)) / factorial(2 * i))
            ans += cal
        print(ans)

def approx_sinh(x, n):
    if n <= 0:
        print(message)

    else:
        ans = 0
        for i in range(0, n):
            cal = (x ** (2 * i + 1)) / factorial(2 * i + 1)
            ans += cal
        print(ans)

def approx_cosh(x, n):
    if n <= 0:
        print(message)

    else:
        ans = 0
        for i in range(0, n):
            cal = (x ** (2 * i)) / factorial(2 * i)
            ans += cal
        print(ans)

if __name__ == '__main__':
    approx_sin(x = 3.14, n = 10)
    approx_cos(x = 3.14, n = 10)
    approx_sinh(x = 3.14, n = 10)
    approx_cosh(x = 3.14, n = 10)
