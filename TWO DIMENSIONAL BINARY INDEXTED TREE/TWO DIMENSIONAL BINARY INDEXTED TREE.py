num_rows = 10
num_columns = 10
def get_number(matrix, sumL): 
 
    for i in range(0, num_columns, 1): 
        sumL[0][i] = matrix[0][i] 
  
     
    for i in range(1, num_rows, 1): 
        for j in range(0, num_columns, 1): 
            sumL[i][j] = matrix[i][j] + sumL[i - 1][j] 
  
     
    for i in range(0, num_rows, 1): 
        for j in range(1, num_columns, 1): 
            sumL[i][j] += sumL[i][j - 1] 

            
def Submatrix_submession(sumL, starting_col, starting_num_rows, ending_num_columns, ending_num_rows): 
    
    result = sumL[ending_num_columns][ending_num_rows] 
    
    if (starting_col > 0): 
        result = result - sumL[starting_col - 1][ending_num_rows] 
  
    
    if (starting_num_rows > 0): 
        result = result - sumL[ending_num_columns][starting_num_rows - 1] 
  
  
    if (starting_col > 0 and starting_num_rows > 0): 
        result = result + sumL[starting_col - 1][starting_num_rows - 1] 
  
    return result 
  
# Driver Code 

matrix = [[51, 42, 63, 24, 86,46, 64, 76, 58, 25], 
          [54, 33, 81, 13, 52,27, 45, 78, 96, 64], 
          [46, 64, 76, 58, 25,9, 49, 63, 2, 8], 
          [27, 45, 78, 96, 64,51, 42, 63, 24, 86],
          [54, 33, 81, 13, 52,59, 49, 63, 2, 8],
          [51, 42, 63, 24, 86,16, 92, 3, 44, 66],
          [51, 42, 63, 24, 86,19, 20, 73, 4, 6],
          [51, 42, 63, 24, 8,91, 2, 33, 9, 2],
          [1, 2, 53, 64, 6,1, 62, 43, 4, 60],
          [59, 49, 63, 2, 8,1, 27, 43, 64, 60]] 

sumL = [[0 for i in range(num_columns)]  
          for j in range(num_rows)] 
  
get_number(matrix, sumL) 
  
starting_col =int(input("Enter starting column number: ")) 
starting_num_rows =int(input("Enter starting Row number: "))
ending_num_columns = int(input("Enter Ending column number: "))
ending_num_rows = int(input("Enter Ending Row number: "))

print("Sum of the Required Matrix is: ", Submatrix_submession(sumL, starting_col, starting_num_rows, ending_num_columns, ending_num_rows))