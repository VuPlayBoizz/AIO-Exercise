import math

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def exercise2():
    x = input("Input x: ")
    if not is_number(x):
        print("x must be a number")
        return
    x = float(x)
    func_name = input("Input activation Function (sigmoid|relu|elu): ").lower()
    
    match func_name:
        case 'sigmoid':
            result = 1 / (1 + math.exp(-x))
            print(f"sigmoid: f({x}) = {result}")
        case 'relu':
            result = max(0, x)
            print(f"relu: f({x}) = {result}")
        case 'elu':
            a = 0.01
            result = x if x > 0 else a * (math.exp(x) - 1)
            print(f"elu: f({x}) = {result}")
        case _:
            print(f"{func_name} is not supported")

if __name__ == '__main__':
    exercise2()