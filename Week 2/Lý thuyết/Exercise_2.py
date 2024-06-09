def character_count (word) :
    character_statistic = {}
    for letter in word:
        count = character_statistic.get(letter,0)
        character_statistic[letter] = count+1

    return character_statistic

assert character_count("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
print(character_count('smiles'))