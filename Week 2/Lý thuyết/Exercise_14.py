def my_function(x):
    return x[::-1]

x = 'I can do it'
assert my_function(x) == "ti od nac I"

x = 'apricot'
print(my_function(x))
