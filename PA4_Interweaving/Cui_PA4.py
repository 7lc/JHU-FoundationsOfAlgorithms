# Cui_PA4 

# Check Interweaving function
def check_interweaving(s, x, y):
    # Initialize the true/false table
    x_length = len(x)
    y_length = len(y)
    table = [[False]*y_length] * x_length
    
    # Counter for time complexity
    counter = 0
    
    # If length s == x == y == 0, return true
    if(len(s) == len(x) == len(y) == 0):
        return True

    # If the lengths of s is less than x and y, return false
    if(len(s) < (x_length + y_length)):
        return False
    
    # Loop through the table
    for i in range(0, x_length):
        for j in range(0, y_length):
            counter = counter + 1
            
            # Empty strings are interweaved, thus set to true
            if(i == 0 and j == 0):
                table[0][0] = True
                
            # If the character in s match both x, y
            elif(i != 0 and j != 0 and x[i-1] == s[i+j-1] and y[j-1] == s[i+j-1]):
                table[i][j] = table[i-1][j] or table[i][j-1]
                
            # If the character in s match character of x
            elif(i != 0 and x[i-1] == s[i+j-1]):
                table[i][j] = table[i-1][j]
                
            # If the character in s match character of y
            elif(j != 0 and y[j-1] == s[i+j-1]):
                table[i][j] = table[i][j-1]
            
    print(counter, " comparison has made.")
    # Return final value
    return table[x_length-1][y_length-1]
    

# Testing 0 - Interweaving
X0 = "101"
Y0 = "0"
S0 = "100010101"

# Testing 1 - Interweaving
X1 = "101"
Y1 = "010"
S1 = "101010101010101"

# Testing 2 - Interweaving
X2 = "101"
Y2 = "010"
S2 = "001100010101010101010111"

# Testing 3 - Interweaving
X3 = "101"
Y3 = "010"
S3 = "100110011001"

# Testing 4 - Not interweaving
X4 = "101"
Y4 = "010"
S4 = "0000000000000"

# Testing 5 - Not interweaving
X5 = "1010"
Y5 = "01"
S5 = "111111"

# Testing 6 - Not interweaving
X6 = "101"
Y6 = "0"
S6 = ""

# Testing all test cases
Xs = [X0, X1, X2, X3, X4, X5, X6]
Ys = [Y0, Y1, Y2, Y3, Y4, Y5, Y6]
Ss = [S0, S1, S2, S3, S4, S5, S6]

for i in range(0, 7):
    print("\n=======Test Case", i, "is Executing=========\n")
    print("X is", Xs[i])
    print("Y is", Ys[i])
    print("S is", Ss[i])

    if(check_interweaving(Ss[i],Xs[i],Ys[i])):
        print("s is in interweaving with x and y\n")
    else:
        print("s is not in interweaving with x and y!!!!! \n")