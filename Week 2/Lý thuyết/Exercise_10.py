def My_function ( integers , number = 1) :
    return any (True if i == number else False for i in integers)

my_list = [1 , 3 , 9 , 4]
assert My_function ( my_list , -1) == False


my_list = [1 , 2 , 3 , 4]
print ( My_function ( my_list , 2) )