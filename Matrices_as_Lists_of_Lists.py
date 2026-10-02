# Matrices as Lists of Lists
# A simple introduction to handling matrices as lists of lists in Python
# Patrick Honner 9/21/22

# Need this to deepcopy lists
import copy

# Makes presenting a table of data easier
from tabulate import tabulate

# We'll hardcode the matrix as a list of lists
# The nested lists function as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

#------------------
# M = [ row_1, row_2, row_3]
# replaced with: 
rows = int(input("Number of rows: "))
M = [list(map(float, input(f"Row {i+1}, separated by spaces: ").split()))
     for i in range(rows)]

print("Here is matrix M shown as a table in Python:\n")
print(tabulate(M))


# Create a new copy of the matrix
# deepcopy creates a copy of values, not a copy of references
N = copy.deepcopy(M)

# Ask user to perform an elementary row operation
#--------------replacing below
#row_choice = input("Choose a row to multiply by a scalar:  ")
#scalar = input("Enter a scalar to multiply by:  ")
#
# Convert row_choice to the appropriate index for the list
#row = int(row_choice) - 1
# Convert the string input to a float
#scalar = float(scalar)

# Perform the elementary row operation
#for i in range(len(N[row])):
#  N[row][i]=scalar*N[row][i]

op = input("Operation (m=multiply, s=swap, a=add): ").lower()
row = int(input("Row to change: ")) - 1

if op == "s":
    other = int(input("Row to swap with: ")) - 1
    N[row], N[other] = N[other], N[row]
elif op in ("m", "a"):
    scalar = float(input("Scalar: "))
    if op == "m":
        if scalar == 0: raise ValueError("Scalar must be nonzero.")
        N[row] = [scalar * x for x in N[row]]
    else:
        other = int(input("Source row: ")) - 1
        if row == other: raise ValueError("Use different rows.")
        N[row] = [x + scalar*y for x, y in zip(N[row], N[other])]
else:
    raise ValueError("Choose m, s, or a.")

print("Here is the new matrix:")
print(tabulate(N))



# A function to print out a list of lists, i.e. a matrix
# tabulate is nicer, so I didn't use this, but left as an example
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")
