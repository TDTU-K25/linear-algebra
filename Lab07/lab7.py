# -*- coding: utf-8 -*-
"""Lab7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qAk9Q8hNjsy__Mdwy6ZbcUhABtFcg8Pz

Exercise 1: Determine if w is a linear combination of the vectors below
"""

from sympy import *
from sympy.solvers.solveset import linsolve
a, b, c, d = symbols('a, b, c, d')

X1a = linsolve([a - b - 3, 2*a + 5*c + 6, 3*a + b - 6*c -17, 4*a + 3*b + 8*c - 11], (a,b,c))
print("X1a =", X1a)

X1b = linsolve([a + 2*b + 2*c, a + 3*b - c - 5, 2*a + 5*b + 3*c - 3, 2*a + 6*b + 6*c], (a,b,c))
print("X1b =", X1b)

X1c = linsolve([a + 2*b + 2*c + 1, a + 3*b - c - 6, 2*a + 5*b + 3*c - 1, 2*a + 6*b + 6*c + 4], (a,b,c))
print("X1c =", X1c)

X1d = linsolve([a - b + d, 2*a + 5*c + 15*d + 6, 3*a + b - 6*c - 12*d - 17, 4*a + 3*b + 8*c + 8*d - 11], (a,b,c,d))
print("X1d =", X1d)

"""Exercise 2: Write program to verify"""

from sympy import *
from sympy.solvers.solveset import linsolve
import numpy as np
a, b, c, d, e = symbols('a, b, c, d, e')

X2a = linsolve([a + c, -2*a - 4*b - c, b + c], (a,b,c))
print("X2a =", X2a)
if (X2a == {(0,0,0)}):
  print("The vectors are linearly independent!")
else:
  print("The vectors aren't linearly independent!")

print()

X2b = linsolve([a + 2*c, b - 2*c, 2*a + 4*b - 4*c], (a,b,c))
print("X2b =", X2b)
if (X2b == {(0,0,0)}):
  print("The vectors are linearly independent!")
else:
  print("The vectors aren't linearly independent!")

x2b = list(X2b)
print("Vector x =", x2b)

print()

X2c = linsolve([a + 2*b - 2*c + 3*d, -2*a + 4*b + 2*d, 3*a + 5*b + d, 4*a + 4*c -d], (a,b,c,d))
print("X2c =", X2c)
if (X2c == {(0,0,0,0)}):
  print("The vectors are linearly independent!")
else:
  print("The vectors aren't linearly independent!")

print()

X2d = linsolve([c + 2*d - e, 2*c + d - 3*e, a + 2*b + 3*c - 5*e, 2*a + 3*b + 4*c, 3*a + b + 5*c], (a,b,c,d,e))
print("X2d =", X2d)
if (X2d == {(0,0,0,0,0)}):
  print("The vectors are linearly independent!")
else:
  print("The vectors aren't linearly independent!")

"""Exercise 3: Let the matrix"""

import numpy as np
C3 = np.array([ [1,0,2,3], [4,-1,0,2], [0,-1,-8,-10] ])
matrix_rank = np.linalg.matrix_rank(C3)
if matrix_rank == 2:
  basic_col = np.array([C3[:,0], C3[:,1]])
  basic_row = np.array([C3[0,:], C3[1,:]])
  print("Basic for the col(C)")
  print(basic_col.T)
  print()
  print("Basic for the row(C)")
  print(basic_row)

"""Exercise 4: Let the matrix"""

from sympy import * 
import numpy as np

A4 = Matrix([ [1 ,0, 2, 3], [4,-1, 0, 2], [0,-1 ,-8, -10] ])
a, b = symbols('a, b')

M = A4.nullspace()
v1, v2= M[0], M[1]
v1 = list(v1)
v2 = list(v2)
M_null = [v1, v2]
print(M_null)

res4 = A4.T * Matrix([ [a * v1[0] - b * v2[0] ], [ a * v1[1] - b * v2[1] ],[ a * v1[2] - b * v2[2] ] ])
print(res4)

"""Exercise 5: Write the program to determine whether w is the column space of A, the null space of A, or
both, where
"""

import numpy as np

def columnSpace(A, w):
    temp = [w]
    for i in range(len(A)):
        temp.append(A[i])
    if len(A) != len(w):
        return False
    if np.linalg.matrix_rank(np.array(A)) < np.linalg.matrix_rank(np.array(temp)):
        return False
    return True 


def checkNullSpace(A, w):
    if len(A) != len(w):
        return False
    if np.sum(np.array(A) * np.array(w)) == 0:
        return True
    return False

def handleEx5(A, w):
    if columnSpace(A, w) and checkNullSpace(A, w):
        print("w is the null space and the column space.")
    elif columnSpace(A, w) and not checkNullSpace(A, w):
        print("w is the column space.")
    elif not columnSpace(A, w) and checkNullSpace(A, w):
        print("w is the null space.")
    else:
        print("w is not The null space and the column space.")

# Câu a
A5a = np.array([[7, 6, -4, 1],
            [-5 ,-1 ,0 ,-2],
            [9, -11, 7, -3],
            [19 ,-9 ,7 ,1]])
w5a = [1,1,-1,-3]
handleEx5(A5a, w5a)

# Câu b
A5b = np.array([[-8, 5, -2, 0],
            [-5, 2, 1, -2],
            [10, -8, 6,-3],
            [3, -2, 1, 0]])
w5b = [1,2,1,0]
handleEx5(A5b, w5b)

"""Exercise 6: Let a1, a2, ...a5 donate the columns of the matrix A, where"""

import numpy as np

A6 = np.array([ [5,1,2,2,0], [3,3,2,-1,-12], [8,4,4,-5,12], [2,1,1,0,-2] ])
a61 = A6[:,0]
a62 = A6[:,1]
a63 = A6[:,2]
a64 = A6[:,3]
a65 = A6[:,4]

B6t1 = np.array([a61, a62, a64, a63]).T
B6t2 = np.array([a61, a62, a64, a65]).T

mrank1 = np.linalg.matrix_rank(B6t1)
mrank2 = np.linalg.matrix_rank(B6t2)
shp1 = B6t1.shape
shp2 = B6t2.shape

# Hạng của ma trận nhỏ hơn kích thước ma trận => vector a3, a5 đó thuộc không gian cột của ma trận B
if mrank1 < shp1[0]:
  print("Rank of matrix is " + str(mrank1) + " < size of matrix = " + str(shp1[0]))
  print("=> a3 is in the column space of B")

print()

if mrank2 < shp2[0]:
  print("Rank of matrix is " + str(mrank2) + " < size of matrix = " + str(shp2[0]))
  print("a5 is in the column space of B")

"""Exercise 7: """

import numpy as np  
v71 = np.array([1,0,2])
v72 = np.array([0,1,4])
v73 = np.array([2,-2,-4])
A7 = np.array([v71, v72, v73])
A7t = A7.T
rank_A7 = np.linalg.matrix_rank(A7t)
print("Dim of vector space =", rank_A7)

print()

if rank_A7 == 2:
  basic_col = np.array([A7t[:,0], A7t[:,1]])
  basic_row = np.array([A7t[0,:], A7t[1,:]])
  print("Basic for the col")
  print(basic_col.T)
  print()
  print("Basic for the row")
  print(basic_row)

"""Exercise 8: Find a basis for the null space of the given matrix A."""

import numpy as np
from scipy.linalg import hilbert
H7 = hilbert(5)
print("H = Hilbert matrix with size 5")
print(H7)

print()

from scipy.linalg import pascal
P7 = pascal(5)
print("P = Pascal matrix with size 5")
print(P7)

"""Exercise 9:"""

import numpy as np
def isOrthogonalSet(A):
    m = A.shape[0]
    n = A.shape[1]
    if (m != n):
        return False
    for i in range(0, n):
        for j in range(0, n):
            sum = 0
            for k in range(0, n):
                sum = sum + (A[i][k] * A[j][k])
        if (i != j and sum != 0):
            return False
    return True
print("-------------------------------------")
u1 = (3,1,1)
u2 = (-1,2,1)
u3 = (-1/2,-2,7/2)
A9 = np.array([u1,u2,u3])
print(A9)
if isOrthogonalSet(A9) :
    print ("Is an orthogonal set")
else :
    print ("Not is an orthogonal set")

"""Exercise 10: Let y and u vector. Write a function to find the orthogonal projection of y on u."""

import numpy as np
def proj_uy(y, u):
  proj_uy = ( (y.dot(u)) / (np.linalg.norm(u,2)**2) ) * u
  return proj_uy

y1 = np.array([7,6])
u1 = np.array([4,2])
k = proj_uy(y1, u1)
print(k)

"""Exercise 11: Let a matrix m × n, write a function to check that has orthonormal columns."""

def isOrthogonal(a, m, n) :
    if (m != n) :
        return False
     
    trans = [[0 for x in range(n)]
                for y in range(n)]
                 
    for i in range(0, n) :
        for j in range(0, n) :
            trans[i][j] = a[j][i]

    prod = [[0 for x in range(n)]
               for y in range(n)]
                
    for i in range(0, n) :
        for j in range(0, n) :
     
            sum = 0
            for k in range(0, n) :
         
                sum = sum + (a[i][k] *
                             a[j][k])
     
            prod[i][j] = sum
 
    for i in range(0, n) :
        for j in range(0, n) :
 
            if (i != j and prod[i][j] != 0) :
                return False
            if (i == j and prod[i][j] != 1) :
                return False
 
    return True
 
a = [[1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]]
         
if (isOrthogonal(a, 3, 3)) :
    print ("Matrix has orthonormal columns")
else :
    print ("Matrix doesn't have orthonormal columns")

"""Exercise 12: Use the Gram - Schmidt process to produce an orthogonal basis for column space of"""

import math
import numpy as np

def find_proj(y, u):
    res = (sum(y*u) / sum(u*u)) * u
    return res

x12 = np.array([[-10,13,7,-11],
              [2,1,5,3],
              [-6,3,13,-3],
              [16,16,2,5],
              [2,1,5,7]])

v12 = np.zeros(x12.shape)
v12[:,0] = x12[:,0]

for i in range(1,len(x12[0])):
    temp = x12[:,i]
    for j in range(i):
        temp = temp - find_proj(x12[:,i], v12[:,j])
    v12[:,i] = temp

print(v12)