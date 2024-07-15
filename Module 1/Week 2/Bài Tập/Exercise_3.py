def word_count_txt(link):
    word_dict = {}
    with open(link, 'r', encoding='UTF-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                count = word_dict.get(word, 0)
                word_dict[word] = count + 1
    print(word_dict)

if __name__ == "__main__":
    path = 'C:/Users/Admin/Desktop/AIO2024/AIO-Exercise/Week 2/P1_data.txt'
    word_count_txt(path)
