import numpy as np

def levenshtein(str1, str2):
    str1 = " " + str1
    str2 = " " + str2
    len_str1 = len(str1)
    len_str2 = len(str2)
    shape = (len_str2, len_str1)
    leve_arr = np.full(shape, fill_value=np.inf)

    for i in range(len_str1):
        leve_arr[0, i ] = i
    for i in range(len_str2):
        leve_arr[i, 0] = i

    for i in range(len_str1-1):
        for j in range(len_str2-1):
            if str1[i+1] == str2[j+1]:
                leve_arr[j+1, i+1] = leve_arr[j, i]
            else:
                leve_arr[j+1, i+1] = np.min(leve_arr[j:j + 2, i:i + 2])+1
    return leve_arr

str1 = "pole"
str2 = "kot"
print(levenshtein(str1, str2))