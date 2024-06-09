def levenshtein_distance(s1, s2):
    matrix = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1,                   
                               matrix[i - 1][j - 1] + substitution_cost)  
            
    distance = matrix[len(s1)][len(s2)]
    return distance



assert levenshtein_distance("hi", "hello") == 4.0
print(levenshtein_distance('hola', 'hello'))