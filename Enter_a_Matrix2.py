# Enter a Matrix2.py Enter a Matrix from user input
# Original code by Patrick Honner, 10/1/2022
# Amended for Challenge 2: manual/file input and RREF

import csv
from fractions import Fraction
from operator import mul as multiply, sub as subtract
from itertools import repeat

M = []
source = input("Matrix source (m=manual, f=file): ").strip().lower()

if source == "f":
    filename = input("File name (for example, matrix.txt): ")
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        M = list(reader)

elif source == "m":
    num_rows = int(input("Enter the number of rows of your matrix: "))
    num_columns = int(input("Enter the number of columns of your matrix: "))
    if num_rows < 1 or num_columns < 1:
        raise ValueError("Use positive numbers of rows and columns.")

    # Initialize as zero; short input rows are amended with zeros
    for i in range(num_rows):
        temp_row = []
        for j in range(num_columns):
            temp_row.append(0.0)
        M.append(temp_row)

    # Read in user input, one row at a time.
    for i in range(num_rows):
        input_row = input("Input row " + str(i) + " separated by commas: ")
        temp_row = input_row.split(",")
        if len(temp_row) > num_columns:
            raise ValueError("Too many entries in this row.")
        for j in range(len(temp_row)):
            M[i][j] = Fraction(temp_row[j])

else:
    raise ValueError("Choose m or f.")

if not M or not M[0] or any(len(row) != len(M[0]) for row in M):
    raise ValueError("The matrix must be nonempty with equal row lengths.")
# Function to print matrix that is a list of lists from Importing_Matricies.py
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):       # M[i][j] is the jth entry in the ith list
            print(A[i][j], "\t", end="") # in other words, it's exactly the ij-th entry in the matrix M
        print("\n")

# Separate matrix using exact fractions, using prior homework code
R = [[Fraction(x) for x in row] for row in M]
num_rows = len(R)
num_columns = len(R[0])

print("\nOriginal matrix:")
print_matrix(R)

i = 0  # The row for the next pivot
for column in range(num_columns):
    if i == num_rows:
        break

    # Find a nonzero entry in this column, at or below row i.
    p = i
    while p < num_rows and R[p][column] == 0:
        p += 1
    if p == num_rows:
        continue  # No pivot here: move to the next column.

    R[i], R[p] = R[p], R[i]  # Swap rows to get the pivot into row i
    pivot = R[i][column]
    R[i] = [x / pivot for x in R[i]]
    for j in range(num_rows):
        if j != i:
            k = R[j][column]
            if k != 0:
                R[j] = list(map(subtract, R[j],
                               map(multiply, repeat(k), R[i])))
    i += 1

print("\nReduced row echelon form:")
print_matrix(R)