def count_substring(string, sub_string):
    M = len(sub_string)
    N = len(string)
    res = 0
     
    # A loop to slide pat[] one by one
    for i in range(N - M + 1):
         
        # For current index i, check
        # for pattern match
        j = 0
        while j < M:
            if (string[i + j] != sub_string[j]):
                break
            j += 1
 
        if (j == M):
            res += 1
    return res

print(count_substring("ABCDCDC", "CDC"))
print(count_substring("BANANA", "A"))
print(count_substring("BANANA", "AN"))