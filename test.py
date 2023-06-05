def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # Создаем матрицу размером (m+1) x (n+1)
    lcs = [[0] * (n + 1) for _ in range(m + 1)]

    # Заполняем матрицу по правилам алгоритма LCS
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs[m][n]

def string_similarity(str1, str2):
    lcs_length = longest_common_subsequence(str1, str2)
    similarity = lcs_length / len(str2)
    return similarity

string1 = "the witcher 3: wild hunt"
string2 = "witchir"
similarity_score = string_similarity(string1, string2)
print(similarity_score)
