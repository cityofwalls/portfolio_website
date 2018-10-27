def hackerrankInString(s):
    global INFINITY
    INFINITY = 9223372036854775807 # sys.maxsize does not work in this skulpt environment for some reason
    hrank = "hackerrank"
    
    result = memoized_lcs_length(hrank, s)
    
    if result == 10:
        return "YES"
    return "NO"
    
def memoized_lcs_length(x, y):
    m, n = len(x), len(y)
    c = []
    for _ in range(m + 1):
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
        
def test():
    test1_input = "hereiamstackerrank"
    test2_input = "hackerworld"
    
    test1_output = "YES"
    test2_output = "NO"

    test1 = [test1_input, test1_output]
    test2 = [test2_input, test2_output]
    
    test = [test1, test2]
    
    printer(test)
    
def printer(test):
    for test_case in test:
        print("Input is", test_case[0])
        print("Expected:", test_case[1])
        print("Result:", hackerrankInString(test_case[0]))
        print()
    
test()