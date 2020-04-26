import numpy as np

def longest_common_substring(s1: str, s2: str):
    n = len(s1)
    m = len(s2)
    max_val = 0
    max_val_row = 0
    max_val_col = 0

    # initialize matrix
    matrix = []
    for i in range(0, n):
        matrix.append([0] * m)

    for row in range(0, n):
        for col in range(0, m):
            # check if the characters match
            if s1[row] == s2[col]:
                # get the value  in the cell that's up and to the left,
                # or 0 if no such cell
                up_left = 0
                if row > 0 and col > 0:
                    up_left = matrix[row-1][col-1]
                
                # set the value for this cell
                matrix[row][col] = 1 + up_left
                if matrix[row][col] > max_val:
                    max_val = matrix[row][col]
                    max_val_row = row
                    max_val_col = col
            else:
                matrix[row][col] = 0
    
    # The longest common substring is the substring
    # in s1 from index max_value_row - max_value + 1
    # up to and including the max_value_col
    start_index = max_val_row - max_val + 1
    return s1[start_index : max_val_col + 1] 


def longest_common_substring_optimized(s1: str, s2: str):
    # Create one row of the matrix.
    n, m = len(s1), len(s2)
    matrix_row = [0] * m

    max_value = 0
    max_value_row = 0

    for row in range(0, n):
        # Var to hold the upper-left value from current matrix position.
        up_left = 0
        for col in range(0, m):
            # Save the current cell's value. This will be up_left
            # for the next iteration.
            saved_current = matrix_row[col]

            # Check if the characters match.
            if s1[row] == s2[col]:
                matrix_row[col] = 1 + up_left

                # Update the saved maximum value and row.
                if matrix_row[col] > max_value:
                    max_value = matrix_row[col]
                    max_value_row = row
            else:
                matrix_row[col] = 0
            
            # Update the up_left variable
            up_left = saved_current
     
    # The longest common substring is the substring
    # in s1 from index max_value_row - max_value + 1
    # up to and including the max_value_col
    start_index = max_value_row - max_value + 1
    return s1[start_index : max_value_row + 1]    

def main():
    substr = longest_common_substring_optimized("look", "zybooks")
    print(substr)

if __name__ == "__main__":
    main()