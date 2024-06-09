def check_the_number ( N ) :
    list_of_numbers = []
    result = ""
    for i in range (1 , 5) :
    #Su dung append them i vao trong list_of_number
        list_of_numbers.append(i)
    if N in list_of_numbers :
        results = " True "
    if N not in list_of_numbers :
        results = " False "
    return results

N = 7
assert check_the_number(N) == " False "
N = 2
results = check_the_number(N)
print(results)