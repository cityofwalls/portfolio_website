def LCS_length(s):
    global INFINITY
    
    # sys.maxsize not working in all environments
    INFINITY = 9223372036854775807
    
    return memoized_lcs_length(s[0], s[1])
    
def memoized_lcs_length(x, y):
    m, n = len(x), len(y)
    c = []
    for row in xrange(m + 1):
        c += [[INFINITY] * (n + 1)]
            
    return lookup_lcs_length(x, y, m, n, c)

def lookup_lcs_length(x, y, i, j, c):
    if c[i][j] < INFINITY:
            return c[i][j]
        
    if i == 0 or j == 0:
        c[i][j] = 0
    elif x[i - 1] == y[j - 1]:
        c[i][j] = lookup_lcs_length(x, y, i - 1, j - 1, c) + 1
    else:
        c[i][j] = max(lookup_lcs_length(x, y, i - 1, j, c),
                      lookup_lcs_length(x, y, i, j - 1, c))
        
    return c[i][j]
        
def __main__():
    test1_input = ["aabaab", "aba"]
    test1_output = 3
    
    test2_input = ["abs", "ppp"]
    test2_output = 0
    
    test3_input = ["green", "eel"]
    test3_output = 2
    
    test4_input = ["marked", "dekram"]
    test4_output = 1
    
    test5_input = ["qwerty", "qwertyu"]
    test5_output = 6

    test1 = [test1_input, test1_output]
    test2 = [test2_input, test2_output]
    test3 = [test3_input, test3_output]
    test4 = [test4_input, test4_output]
    test5 = [test5_input, test5_output]
    
    test = [test1, test2, test3, test4, test5]
    
    tester(test)
    
def tester(test):
    for test_case in test:
        print("Input is", test_case[0])
        print("Expected:", test_case[1])
        print("Result:", LCS_length(test_case[0]))
        print()
    
if __name__ is "__main__": __main__()