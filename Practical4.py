"""
PRACTICAL NO: 4
NUMPY OPERATIONS

Lab Assignment - 1
Lab Assignment - 2
"""

import numpy as np


# ==========================================
# LAB ASSIGNMENT - 1
# ==========================================

print("LAB ASSIGNMENT - 1")

# ------------------------------------------
# (a) Generate a 4x4 Identity Matrix
# ------------------------------------------

print("\n(a) 4x4 Identity Matrix:")

identity_matrix = np.eye(4)
print(identity_matrix)


# ------------------------------------------
# (b) Two 3x3 Random Matrices (1 to 9)
#     Matrix Addition and Multiplication
# ------------------------------------------

print("\n(b) 3x3 Random Matrices (values 1-9):")

matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix Addition
addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

# Matrix Multiplication
multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)


# ==========================================
# LAB ASSIGNMENT - 2
# ==========================================

print("\nLAB ASSIGNMENT - 2")

print("\nMultiply a 5x3 Matrix by a 3x2 Matrix")

# Take input from user for 5x3 matrix
print("\nEnter elements for 5x3 matrix:")
matrixA = []
for i in range(5):
    row = list(map(int, input(f"Enter 3 elements for row {i+1}: ").split()))
    matrixA.append(row)

matrixA = np.array(matrixA)

# Take input from user for 3x2 matrix
print("\nEnter elements for 3x2 matrix:")
matrixB = []
for i in range(3):
    row = list(map(int, input(f"Enter 2 elements for row {i+1}: ").split()))
    matrixB.append(row)

matrixB = np.array(matrixB)

print("\nMatrix A (5x3):")
print(matrixA)

print("\nMatrix B (3x2):")
print(matrixB)

# Matrix Multiplication
product = np.dot(matrixA, matrixB)

print("\nProduct Matrix (5x2):")
print(product)
