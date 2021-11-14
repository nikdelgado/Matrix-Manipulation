# Author: Nik Delgado
# Class: CS 2300
# Project 1
# Description: This program reads in a data file and stores the numbers in the data file into a matrix. The program then applies an equation to the matrix and writes the output to a file. The program also transposes the matrix and writes the result to another file.

import numpy as np

# Open the Matrix File
f = open("matrixFile.txt", "r")

# Break each line into strings
contents = f.readlines()
f.close()

# Store the second line as string A and clean up the formatting
StrA = contents[1]
StrA = StrA.replace(" ", "")
StrA = ','.join(StrA).replace('-,', '-')
listA = StrA.split(',')

# Write the formatted string to a file
w = open("FirstMatrix.txt", "w")
w.write(StrA[:-2])
w.close()

# store Row and col size in variables
rowSizeA = int(StrA[2])
colSizeA = int(StrA[4])

# convert string of data to a list for A
StrA = StrA[6:-2]
listA = StrA.split(',')
listA = [int(i) for i in listA]

# Store the second line as string B and clean up the formatting
StrB = contents[2]
StrB = StrB.replace(" ", "")
StrB = ','.join(StrB).replace('-,', '-')

# Write the formatted string to a file
w = open("SecondMatrix.txt", "w")
w.write(StrB)
w.close()

# store Row and col size in variables
rowSizeB = int(StrB[2])
colSizeB = int(StrB[4])

# convert string of data to a list for B
StrB = StrB[6:]
listB = StrB.split(',')
listB = [int(i) for i in listB]


# Create two matrices
matrixA = np.ndarray(shape=(rowSizeA, colSizeA), dtype=int)
matrixB = np.ndarray(shape=(rowSizeB, colSizeB), dtype=int)

# Store data from list A into matrix A
count = 0
for i in range(rowSizeA):
    for z in range(colSizeA):
        matrixA[i][z] = listA[count]
        count += 1

# Store data from list B into matrix B
count = 0
for i in range(rowSizeB):
    for z in range(colSizeB):
        matrixB[i][z] = listB[count]
        count += 1

# Print the contents of each matrix
print("Matrix A")
print(matrixA, "\n")
print("Matrix B")
print(matrixB, "\n")

# calculate C = 10.5B-8.0A
print("Calculate C with each item in both matrices")

w = open("calcMatrix.txt", "w")
w.write("C, ")
w.write(str(rowSizeA))
w.write(", ")
w.write(str(colSizeA))
w.write(", ")


for i in range(rowSizeA):
    for z in range(colSizeA):
        c = 10.5 * (matrixB[i][z]) - 8.0 * (matrixA[i][z])
        print(c)
        w.write(str(c))

        if i != rowSizeA and z != colSizeA - 1:
            w.write(", ")

w.close()

# Transpose second matrix

print("\nTransposed second matrix")
print(matrixB.T)
w = open("transposedMatrix.txt", "w")
w.write("B, ")
w.write(str(rowSizeB))
w.write(", ")
w.write(str(colSizeB))
w.write(", ")

for i in range(rowSizeB):
    for z in range(colSizeB):
        w.write(str(matrixB[i][z]))

        if i != rowSizeA and z != colSizeA - 1:
            w.write(", ")

w.close()
