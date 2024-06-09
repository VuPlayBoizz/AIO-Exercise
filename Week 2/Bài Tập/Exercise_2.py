def count_char(string):

    char_count = {}
    for char in string:
        count = char_count.get(char, 0)
        char_count[char] = count + 1
    
    print(char_count)

if __name__ == "__main__":
    string = 'Happiness'
    count_char(string= string)
    
    