def max_sliding_window():
    result = []
    Array = []
    n = int(input("Nhap so luong phan tu cua mang: "))
    for i in range(0, n):
        A_i = int(input(f"Nhap phan tu thu {i + 1}: "))
        Array.append(A_i)
        
    k = int(input("Nhap kich thuoc k: "))
    
    for i in range(len(Array) - k + 1):
        max_value = max(Array[i:i + k])
        result.append(max_value)
        
    for value in result:
        print(value)

if __name__ == "__main__":
    max_sliding_window()
    