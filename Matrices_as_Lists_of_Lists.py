# Matrices as Lists of Lists
# A simple introduction to handling matrices as lists of lists in Python
# Patrick Honner 9/21/22

# Need this to deepcopy lists
import copy
from fractions import Fraction
from operator import mul as multiply, sub as subtract  # this and below for substracting list multiplied by a coefficient from another
from itertools import repeat

# Makes presenting a table of data easier
from tabulate import tabulate



R = [[Fraction(x) for x in row]
     for row in [[3, -4, 0, 5], [-1, -2, 3, 10], [4, 1, 1, 3]]]


for i in range(3):
    pivot = R[i][i]
    R[i] = [x / pivot for x in R[i]]
    for j in range(3):
        if j != i:
            k = R[j][i]
            R[j] = list(map(subtract, R[j], 
                                      map(multiply, repeat(k), R[i])
                            )
                        )   # list - turns result into list, map(function, list1, list2) does function/operation pairwise to respective elements of two lists
# can be written as  R[j] = [x - k*y for x, y in zip(R[j], R[i])]

print("\nRREF of the original hard-coded matrix:")
for row in R:
    print("\t".join(map(str, row)))


# We'll hardcode the matrix as a list of lists
# The nested lists function as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]


M = [ row_1, row_2, row_3]

if input("Matrix (h=hard-coded, u=user-entered): ").strip().lower() == "u":
    rows = int(input("Number of rows: "))
    M = [list(map(float, input(f"Row {i+1}, separated by spaces: ").split()))
         for i in range(rows)]

# new code: 
#rows = int(input("Number of rows: "))
#M = [list(map(float, input(f"Row {i+1}, separated by spaces: ").split()))
#     for i in range(rows)]

print("Here is matrix M shown as a table in Python:\n")
print(tabulate(M))


# Create a new copy of the matrix
# deepcopy creates a copy of values, not a copy of references
N = copy.deepcopy(M)

# Ask user to perform an elementary row operation
while True:
    op = input("r=row, c=column, e=entry, m=multiply, s=swap, a=add, q=quit: ").strip().lower()
    if op == "q": break

    if op == "c":
        column = int(input("Column number: ")) - 1
        print("Column:", [r[column] for r in N])
    else:
        row = int(input("Row number: ")) - 1
        if op == "r":
            print("Row:", N[row])
        elif op == "e":
            column = int(input("Column number: ")) - 1
            N[row][column] = float(input("New value: "))
        elif op == "s":
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
            raise ValueError("Choose r, c, e, m, s, a, or q.")

    print(tabulate(N))
    if input("Type more to continue or exit: ").strip().lower() != "more": break



# A function to print out a list of lists, i.e. a matrix
# tabulate is nicer, so I didn't use this, but left as an example
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")
