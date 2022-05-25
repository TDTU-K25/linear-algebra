# -*- coding: utf-8 -*-
"""Lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ppcT9Vb_5sgVNN6f0_kad5cayb0hRVaL

Exercise 1: Using a command to create the new matrices from vectors
"""

import numpy as np
x1 = np.array([1,2,3,4,5])
b1 = np.array([1,2,3,4,5,6])

print("a)")
print("Matrix before transpose:")
A1 = np.array([x1,x1,x1,x1,x1])
print(A1)

print()

print("Matrix after transpose:")
print(np.transpose(A1))

print()

print("b)")
print("Matrix B:")
B1 = np.array([b1,b1,b1,b1,b1,b1])
print(B1)

print()

print("c)")
c1 = []
for i in range(1, 31, 1):
  c1.append(i)
C1 = np.array(c1).reshape(6,5)
print("Matrix before transpose:")
print(C1)

print()

print("Matrix after transpose:")
print(C1.T)

print()

print("d)")
d1 = []
for i in range(1, 26, 1):
  d1.append(i)
D1 = np.array(d1).reshape(5,5)
print("Matrix D:")
print(D1)

"""Exercise 2: Write a command that will create a 5×6 matrix with random integer entries with the elements ∈ [a, b], where a, b ∈ Z"""

import numpy as np
print("5x6 Matrix:")
randomMatrix = np.random.randint(100, size=(5,6))
print(randomMatrix)

"""Exercise 3: Write a command to flip the matrix horizontally"""

import numpy as np 

a3 = []
for i in range(1, 10, 1):
  a3.append(i)
A3 = np.array(a3).reshape(3,3)
print("The original matrix:")
print(A3)

print()

print("Matrix after flip horizontally")
A3h = np.flip(A3,1) # horizontal flip (lật ngang)
print(A3h)

"""Exercise 4: Write a command to flip the matrix vertically"""

import numpy as np 

a4 = []
for i in range(1, 10, 1):
  a4.append(i)
A4 = np.array(a4).reshape(3,3)
print("The original matrix:")
print(A4)

print()

print("Matrix after flip vertically")
A4v = np.flip(A4,0) # flip vertical flip (lật dọc)
print(A4v)

"""Exercise 5: Enter the matrix, provide a command to create vectors or matrices as follows"""

import numpy as np
Y5 = np.array([ [1,2,16,31,22], [2,8,12,21,23], [4,9,11,14,25], [3,6,10,16,34] ])

x5 = np.array(Y5[1, 1:4]) # lấy phần tử thứ 2, thứ 3, thứ 4 ở dòng số 2
print("x =",x5)

print()

y5 = np.array(Y5[:, 2]) # lấy hết phần tử ở cột 3
y5T = y5.reshape(len(y5),1)
print("y =", y5T)

print()

A5 = np.array([ Y5[1, 1:4], Y5[2, 1:4] ]) # lấy phần tử thứ 2, thứ 3, thứ 4 ở dòng số 2 và 3
print("A =", A5)

print()

B5 = np.array([ Y5[:, 0], Y5[:, 2], Y5[:, 4] ]) # lấy hết phần tử ở cột 1, 3, 5 
print("B =", B5.T)

print()

C5 = np.array([ Y5[1:, 0], Y5[1:, 2], Y5[1:, 3], Y5[1:, 4]]) # lấy phần tử thứ 2, thứ 3, thứ 4 ở cột 1, 3, 4, 5 
print("C =", C5.T)

print()
D5 = []
for i in range(0, len(Y5), 1):
  for j in range(0, len(Y5[0]), 1):
    if (Y5[i][j] > 12):
      D5.append(Y5[i][j])
D5 = np.array(D5)
print("D =", D5.reshape(3,3))

"""Exercise 6: Given the matrix A, provide commands to do the following:"""

import numpy as np 
A6 = np.array([ [2,4,1], [6,7,2], [3,5,9]])

x6 = A6[0, :]
print("x1 =", x6)

print()

Y6 = np.array([ A6[1, :], A6[2, :]])
print("Y =",Y6)

"""Exercise 7: Let A. Write command that will:"""

import numpy as np 
A7 = np.array([ [2,7,9,7], [3,1,5,6], [8,1,2,5]])

B7 = np.array([ A7[:, 1], A7[:, 3]]) # Lấy cột thứ 2 và 4
B7 = B7.reshape(1, 6) # matrix
B7 = B7[0, :] # vector
print("B =", B7)

print()

C7 = np.array([ A7[:, 0], A7[:, 2]]) # Lấy cột thứ 1 và 3
C7 = C7.reshape(1, 6) # matrix
C7 = C7[0, :] # vector
print("C =", C7)

print()

A7 = A7.reshape(4,3)
print("A =", A7)

"""Exercise 8: A local shop sells three types of ice cream flavours: strawberry, vanilla and chocolate. Straw-berry costs 2 dollars, vanilla 1 dollars and chocolate 3 dollars each. The sales of each ice cream are as show in the following table."""

import numpy as np
SVC = np.array([[2,1,3]]) # Ma trận 1x3 giá của các loại kem: strawberry, vanilla và chocolate
DS = np.array([ [12,5,8], [15,9,12], [10,14,10], [16,7,9], [12,10,15]]) # ma trận doanh số từng ngày
DS_T = DS.T # chuyển vị ma trận 5x3 thành 3x5
TDT = SVC.dot(DS_T) # nhân 2 ma trận thu đc ma trận 1x5 tổng doanh thu
print("Tổng doanh thu của sản phẩm mỗi ngày:", TDT[0])

"""Exercise 9: Let T be a (transition) matrix of a Markov chain and p be a probability vector. Then the probability that the chain is in a particular state after k steps is given by the vector pk:"""

import numpy as np
T9 = np.array([ [0.6,0.7], [0.4,0.3] ])
p9 = np.array([ [0.5], [0.5] ])
list_k = [1,2,10,100,10000]

# Luỹ thừa ma trận
# np.linalg.matrix_power

# User-defined function
def powMatrix(matrix, k):
  originalMatrix = matrix
  matrixAfterPow = matrix 
  for i in range (2, k+1, 1):
    matrixAfterPow = matrix.dot(originalMatrix)
    matrix = matrixAfterPow
  return matrixAfterPow

for k in list_k:
  matrixT_AfterPow = np.linalg.matrix_power(T9, k)
  result = matrixT_AfterPow.dot(p9)
  print("p" + str(k) + ":")
  print(result)
  print()

"""Exercise 10:"""

import numpy as np
A10 = np.array([ [-1,4,8], [-9,1,2]])
B10 = np.array([ [5,8], [0,-6], [5,6]])
C10 = np.array([ [-4,1], [6,5]])
D10 = np.array([ [-6,3,1], [8,9,-2], [6,-1,5]])

def multiplyMatrix(X, Y):
  if (len(X[0]) == len(Y)):
    result = X.dot(Y)
    return result

def subMatrix(X, Y):
  if (len(X) == len(Y) and len(X[0] == len(Y[0]))):
    result = X - Y
    return result

def addMatrix(X, Y):
  if (len(X) == len(Y) and len(X[0] == len(Y[0]))):
    result = X + Y
    return result

print("a)")
if (multiplyMatrix(A10, B10.T) == None):
  print("Không thể nhân 2 ma trận")
else:
  print(multiplyMatrix(A10, B10.T))

print()

print("b)")
print(multiplyMatrix(B10, C10.T))

print()

print("c)")
print(subMatrix(C10, C10.T))

print()

print("d)")
print(subMatrix(D10, D10.T))

print()

print("e)")
print((D10.T).T)

print()

print("f)")
print(2*C10.T)

print()

print("g)")
print(addMatrix(A10.T, B10))

print()

print("h)")
print(addMatrix(A10.T, B10).T)

print()

print("i)")
print(subMatrix(2*A10.T, 5*B10).T)

print()

print("j)")
print(((-1)*D10).T)

print()

print("k)")
print((-1) * D10.T)

print()

print("l)")
print((multiplyMatrix(C10, C10).T))

print()

print("m)")
print((multiplyMatrix(C10.T, C10.T)))

"""Exercise 11:"""

import numpy as np

# Tính vết của ma trận:
# traceMatrix = np.trace(matrix)

# Tính hạng của ma trận
# rankMatrix = np.linalg.matrix_rank(matrix)

def isSquare(X):
  dimensionOfMatrix = X.shape # Số chiều của ma trận 
  if(dimensionOfMatrix[0] == dimensionOfMatrix[1]):
    return True
  else:
    return False

def printUpperTriangleOfMatrix(X):
  for i in range(0, len(X), 1):
    for j in range(0, len(X[0]), 1):
      if (i <= j):
        print(str(X[i][j]) + " ", end = " ")
      else:
        print("  ", end = " ")
    print()

def printLowerTriangleOfMatrix(X):
  for i in range(0, len(X), 1):
    for j in range(0, len(X[0]), 1):
      if (i >= j):
        print(str(X[i][j]) + " ", end = " ")
      else:
        print("  ", end = " ")
    print()

def isSymetricMatrix(X):
  XT = X.T
  for i in range (0, len(X), 1):
    for j in range (0, len(X[0]), 1):
      if (X[i][j] != XT[i][j]):
        return False 
  return True

def isSkewSymetricMatrix(X):
  X = (-1) * X
  XT = X.T
  for i in range (0, len(X), 1):
    for j in range (0, len(X[0]), 1):
      if (X[i][j] != XT[i][j]):
        return False 
  return True

A11 = np.array([ [2,4,1], [6,7,2], [3,5,9] ])
# a)
if (isSquare(A11)):
  print("Matrix A is square matrix")

print()

# b)
if (isSymetricMatrix(A11)):
  print("Matrix A is symetric matrix")
else:
  print("Matrix A isn't symetric matrix")

print()

# c)
if (isSkewSymetricMatrix(A11)):
  print("Matrix A is skew-symetric matrix")
else:
  print("Matrix A isn't skew-symetric matrix")

print()

# d)
print("Upper Triangle Of Matrix:")
printUpperTriangleOfMatrix(A11)

print()

# e)
print("Lower Triangle Of Matrix:")
printLowerTriangleOfMatrix(A11)

"""Exercise 12: Write a command to compute the determinant of the matrices below:"""

import numpy as np
def computeDet(X):
  if (len(X) == len(X[0])):
    detX = np.linalg.det(X)
  else:
    return False;
  return round(detX,2)

A12 = np.array([ [6,0,0,5], [1,7,2,-5], [2,0,0,0], [8,3,1,8] ])
print("det(A) =", computeDet(A12))

B12 = np.array([ [1,-2,5,2], [0,0,3,0], [2,-6,-7,5], [5,0,4,4] ])
print("det(B) =", computeDet(B12))

C12 = np.array([ [3,5,-8,4], [0,-2,3,-7], [0,0,1,5], [0,0,0,2] ])
print("det(C) =", computeDet(C12))

D12 = np.array([ [4,0,0,0], [7,-1,0,0], [2,6,3,0], [5,-8,3,0], [5,-8,4,-3] ])
if (computeDet(D12)):
  print("det(D) =", computeDet(D12))
else:
  print("Can't compute determinant of matrix")

E12 = np.array([ [4,0,-7,3,-5], [0,0,2,0,0], [7,3,-6,4,-8], [5,0,9,-1,2], [0,0,9,-1,2]])
print("det(E) =", computeDet(E12))

F12 = np.array([ [6,3,2,4,0], [9,0,-4,1,0], [8,-5,6,7,1], [3,0,0,0,0], [4,2,3,2,0] ])
print("det(F) =", computeDet(F12))

"""Exercise 13: Is it true that det(A + B)=detA+detB? To find out, generate random 5 × 5 matrices A and B, and compute det(A + B)−detA−detB. Repeat the calculations for three other pairs of n × n matrices, for various values of n."""

import numpy as np
import random

def prove(n):
  A = np.random.randint(-5, 5, size = (n, n))
  B = np.random.randint(-5, 5, size = (n, n))

  det_A_plus_B = np.linalg.det(A + B)
  detA = np.linalg.det(A)
  detB = np.linalg.det(B)

  if (det_A_plus_B - detA - detB == 0):
    print("det(A+B) == detA + detB")
  else:
    print("det(A+B) != detA + detB")

for i in range(1, 5, 1):
  if (i == 1):
    n = 5
  else:
    n = random.randrange(2,10)
  print("n =", n)
  prove(n)

"""Exercise 14: Is it true that detAB=(detA)(detB)? Repeat the calculation for four pairs of random ma-trices."""

import numpy as np
import random

def prove(n):
  A = np.random.randint(-5, 5, size = (n, n))
  B = np.random.randint(-5, 5, size = (n, n))

  detAB = np.linalg.det(A.dot(B))
  detA = np.linalg.det(A)
  detB = np.linalg.det(B)

  if (round(detAB,2) == round(detA * detB, 2)):
    print("det(AB) == detA * detB")
  else:
    print("det(AB) != detA * detB")

for i in range(1, 5, 1):
  n = random.randrange(2,10)
  print("n =", n)
  prove(n)

"""Exercise 15: Let A and B be the following 3 × 3 matrices"""

import numpy as np

A15 = np.array([ [2, 4, 5.0/2], [-3.0/4, 2, 1.0/4], [1.0/4, 1.0/2, 2] ])
B15 = np.array([ [1, -1.0/2, 3.0/4], [3.0/2, 1.0/2, -2], [1.0/4, 1, 1.0/2] ])
inv_A15 = np.linalg.inv(A15)
inv_B15 = np.linalg.inv(B15)

# a)
print("A^(-1) * B^(-1) =", inv_A15.dot(inv_B15))

print()

print("(AB)^(-1) =", np.linalg.inv(A15.dot(B15)))

print()

print("(BA)^(-1) =", np.linalg.inv(B15.dot(A15)))

print()

# b)
print("Transpose of A^(-1)", inv_A15.T)

print()

print("Inversion of transpose A", np.linalg.inv(A15.T))