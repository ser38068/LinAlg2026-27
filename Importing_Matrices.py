# Load Data into a Matrix, Patrick Honner 10/1/2022
# Simple example of reading a csv file in and converting to a list of lists


# Import the csv module for handling data
import csv

# This reads in the comma separated values as a list of lists of strings
#                                               Each line is a list

with open("matrix.txt") as f:
  reader = csv.reader(f)
  d = list(reader)

print("The original lists of lists:")
print(d)
print("\n")

# By default lists have strings as entries, so convert them to floats

for i in range(len(d)):
  for j in range(len (d[i])):
    d[i][j]=float(d[i][j])


print("The list of lists of floats")
print (d)
print("\n")

# A function to print out a list of lists, i.e. a matrix
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")

print("In a 'matrix' format:")
print_matrix(d)

def is_row_echelon_form(R):
    previous_pivot = -1

    for i in range(len(R)):
        
        pivot_column = len(R[i])  # This is zero if list of lists R is empty as in R=[[]] 
                                  # and above loop runs but below loop does not run
        for j in range(len(R[i])):
            if R[i][j] != 0:
                pivot_column = j
                break  # need the first nonzero element in row i

        # A nonzero row's pivot must be strictly to the right of that for the row above
        if pivot_column < len(R[i]) and pivot_column <= previous_pivot:
            return False

        previous_pivot = pivot_column

    return True


print("Row echelon form:", is_row_echelon_form(d))