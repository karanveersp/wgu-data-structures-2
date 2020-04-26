# Greedy Algorithms

A greedy algorithm is an algorithm that, when presented with a list of options, chooses the option that is optimal at that point in time.
The choice of option does not consider additional subsequent options, and may or may not lead to an optimal solution.

Ex. Knapsack, Activies and Make Change algorithms.

# Dynamic Programming

Dynamic programming is a problem solving technique that splits a problem into smaller subproblems, computes and stores solutions to subproblems in memory, and then uses the stored solutions to solve the larger problem.

The primary characteristic of DP is the storage and reuse of computed results to reduce recomputation in future calculations.

Ex. Fibonacci numbers can be computed with an iterative approach that stores the 2 previous terms, instead of making recursive calls that recompute the same term many times over.

---

The longest common substring algorithm takes 2 strings as input and determines the longest substring that exists in both strings.

* An NxM int matrix keeps track of matching substrings, where N is the length of the first string and M the length of the second.

* Each row is a character from the first string, and each column represents a character from the second string.

* An entry at i,j in the matrix indicates the length of the longest common substring that ends at character i in the first string and character j in the second. An entry will be 0 only if the two characters the entry corresponds to are not the same.

* The matrix is built one row at a time, from the top row to the bottom row. Each row's entries are filled from left to right. An entry is set to 0 if the two characters do not match. Otherwise, the entry at i,j is set to 1 plus the entry in i-1, j-1 or upper left cell.

* The start index in str1 is `max_val_row - max_val + 1`. The end index in str1 is `max_val_col + 1`.

* The algorithm can be space optimized since only the previous row is required to access the upper left value.

