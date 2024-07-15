import random
import math

def exercise3():
    num_samples = input("Input number of samples ( integer number ) which are generated: ")
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    num_samples = int(num_samples)
    
    loss_name = input("Input loss name :").upper()
    
    match loss_name:
        case 'MSE':
            total = 0
            for i in range(0, num_samples):            
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss = (target - predict) ** 2
                total += loss
                print(f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}')
            return print(f'final MSE: {total / num_samples}')
        case 'MAE':
            total = 0
            for i in range(0, num_samples):
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss = abs(target - predict)
                total += loss
                print(f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}')
            return print(f'final MAE: {total / num_samples}')
        case 'RMSE':
            total = 0
            for i in range(0, num_samples):
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss = (target - predict) ** 2
                total += loss
                print(f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}')
            return print(f'final RMSE: {math.sqrt(total / num_samples)}')
        case _:
            return print("Invalid regression loss function")
    
    
if __name__ == '__main__':
    exercise3()