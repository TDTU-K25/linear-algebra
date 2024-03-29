# -*- coding: utf-8 -*-
"""Lab6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u2fFUDfb20oZFjoI-w3Puc2AgznUGDIt

Exercise 1: Write command to find 1-norm of the following matrices:
"""

import numpy as np

def norm_1(a):
  arrayOfSumOfElementsInColumn = []
  for j in range(0, len(a[0])):
    sum = 0
    for i in range(0, len(a)):
      sum += abs(a[i][j])
      arrayOfSumOfElementsInColumn.append(sum)

  max = arrayOfSumOfElementsInColumn[0]
  for item in arrayOfSumOfElementsInColumn:
    if (item > max):
      max = item
  return max

A1 = np.array([ [1,-7], [-2,-3]])
print("a)", np.linalg.norm(A1, 1))

A2 = np.array([ [-2,8], [3,1]])
print("b)", np.linalg.norm(A2, 1))

A3 = np.array([ [2,-8], [3,1]])
print("c)", np.linalg.norm(A3, 1))

A4 = np.array([ [2,3], [1,-1]])
print("d)", np.linalg.norm(A4, 1))

A5 = np.array([ [5,-4,2], [-1,2,3], [2,1,0]])
print("e)", np.linalg.norm(A5, 1))

"""Exercise 2: Write command to find infinity-norm of the following matrices:"""

import numpy as np

def norm_inf(a):
  arrayOfSumOfElementsInRow = []
  for i in range(0, len(a)):
    sum = 0
    for j in range(0, len(a[i])):
      sum += abs(a[i][j])
      arrayOfSumOfElementsInRow.append(sum)

  max = arrayOfSumOfElementsInRow[0]
  for item in arrayOfSumOfElementsInRow:
    if (item > max):
      max = item
  return max

B1 = np.array([ [1,-7], [2,3] ])
print("a)", np.linalg.norm(B1, np.inf))

B2 = np.array([ [3,6], [1,0] ])
print("b)", np.linalg.norm(B2, np.inf))

B3 = np.array([ [5,-4,2], [1,2,3], [-2,1,0] ])
print("c)", np.linalg.norm(B3, np.inf))

B4 = np.array([ [3,6,-1], [3,1,0], [2,4,-7] ])
print("d)", np.linalg.norm(B4, np.inf))

B5 = np.array([ [-3,0,0], [0,4,0], [0,0,2] ])
print("e)", np.linalg.norm(B5, np.inf))

"""Exercise 3: Write command to find calculate the Frobenius-norm"""

import numpy as np

def norm_fro(a):
  sum = 0
  for i in range(0, len(a)):
    for j in range(0, len(a[i])):
      sum += pow(a[i][j], 2)
  return np.sqrt(sum)

C1 = np.array([ [5,-4,2], [1,2,3], [-2,1,0] ])
print("a)", np.linalg.norm(C1, 'fro'))

C2 = np.array([ [1,7,3], [4,-2,-2], [-2,-1,1] ])
print("b)", np.linalg.norm(C2, 'fro'))

C3 = np.array([ [2,3], [1,-1]])
print("c)", np.linalg.norm(C3, 'fro'))

"""Exercise 4: Let u and v be vectors in R2. For the following u and v determine the angle between the vectors."""

import math
import numpy as np 

def angle(u,v):
  uv = u.dot(v) # tích vô hướng của vector u và vector v
  mag_u = np.linalg.norm(u, 2) # Độ lớn của vector u
  mag_v = np.linalg.norm(v, 2) # Độ lớn của vector u
  cos_x = uv / (mag_u*mag_v)
  return cos_x

u_a = np.array([1,1])
v_a = np.array([0,1])
print("a)", angle(u_a,v_a))

u_b = np.array([1,0])
v_b = np.array([0,1])
print("b)", angle(u_b,v_b))

u_c = np.array([-2,3])
v_c = np.array([1/2,-1/2])
print("c)", angle(u_c,v_c))

"""Exercise 5: Determine the unit vector uˆ for each of the following vectors."""

import numpy as np 

def findUnitOfVector(u):
  mag_u = np.linalg.norm(u, 2)
  unit_u = (1/mag_u) * u
  return unit_u

u5a = np.array([2, 3])
print("a)", findUnitOfVector(u5a))

u5b = np.array([1, 2, 3])
print("b)", findUnitOfVector(u5b))

u5c = np.array([1/2, -1/2, 1/4])
print("c)", findUnitOfVector(u5c))

u5d = np.array([np.sqrt(2), 2, -np.sqrt(2), np.sqrt(2)])
print("d)", findUnitOfVector(u5d))

"""Exercise 6: Find the Euclidean distances between satellites."""

import numpy as np
v1 = np.array([1, 2, 3])
s2 = np.array([7, 4, 3])
s3 = np.array([2, 1, 9])
mag_v1s2 = np.linalg.norm(s2 - v1, 2)
mag_v1s3 = np.linalg.norm(s3 - v1, 2)
mag_s2s3 = np.linalg.norm(s3 - s2, 2)

print("Khoảng cách giữa vector v1 và vector s2:", mag_v1s2)
print("Khoảng cách giữa vector v1 và vector s3:", mag_v1s3)
print("Khoảng cách giữa vector s2 và vector s3:", mag_s2s3)

"""Exercise 7: Write a function to decode the encoded following message"""

import numpy as np

E = np.array([ [80,98,99,85,106,94], [71,92,76,95,100,92], [124,163,140,160,176,161] ])
A = np.array([ [1,2,3], [2,1,2], [3,2,4] ])

inv_A = np.linalg.inv(A)
D = inv_A.dot(E)
D_transpose = D.T

listUpperCaseChar = list(map(chr, range(97 - 32, 123 - 32)))
listUpperCaseChar.append(" ") # thêm kí tự space
s = ""
for i in range(0, len(D_transpose)):
    for j in range(0, len(D_transpose[i])):
        k = int(round(D_transpose[i][j],0))
        s = s + listUpperCaseChar[k - 4] 
print(s)

"""Exercise 8: Using lookup table in the Exercise 8, write a function to encode the following message"""

import numpy as np

A = np.array([ [3,4,5], [1,3,1], [1,1,2] ])

listUpperCaseChar = list(map(chr, range(97 - 32, 123 - 32)))
listUpperCaseChar.append(" ") # thêm kí tự space

msg1 = "ATTACK"
msg2 = "LINEAR ALGEBRA LABORATORY"

def encodeMessage(msg, encodingMatrix):
  E = [] 
  numbersOfCol = 0
  listCharsOfMsg = list(msg) # convert string to list of characters

  for i in range (0, len(listCharsOfMsg)): # loop through each character of msg
    for j in range (0, len(listUpperCaseChar)): # loop through each character in alphabet
      if listCharsOfMsg[i] == listUpperCaseChar[j]: 
        E.append(j)

  if (len(E) % 3 == 0):
    numberOfCols = int(len(E) / 3)
    E = np.array(E).reshape(3, numberOfCols)
  else:
    while (len(E) % 3 != 0):
      E.append(27) # add character key of space
    numberOfCols = int(len(E) / 3)
    E = np.array(E).reshape(3, numberOfCols)

  msgAfterEncode = encodingMatrix.dot(E)
  return msgAfterEncode.flatten() # convert to 1D array

print("\"ATTACK\" after encode:",encodeMessage(msg1, A))
print()
print("\"LINEAR ALGEBRA LABORATORY\" after encode:",encodeMessage(msg2, A))

"""Exercise 9: Write a function to calculate the similarities among documents. Consider the following document-term matrix"""

import numpy as np

doc1 = np.array([0,4,0,0,0,2,1,3])
doc2 = np.array([3,1,4,3,1,2,0,1])
doc3 = np.array([3,0,0,0,3,0,3,0])
doc4 = np.array([0,1,0,3,0,0,2,0])
doc5 = np.array([2,2,2,3,1,4,0,2])
A9 = np.array([ doc1, doc2, doc3, doc4, doc5 ])

rank_A9 = np.linalg.matrix_rank(A9)
  
for i in range (0, rank_A9):
  for j in range (0, rank_A9):
    cos_sim = np.dot(A9[i], A9[j]) / (np.linalg.norm(A9[i]) * np.linalg.norm(A9[j]))
    print("Cosine Similairty [",i,j,"] = ", round(cos_sim, 2))
  print()

"""Exercise 10: Write a function reuse the Cosine Similarity measure to retrieve the documents which is the nearest with vector q = (0 0 0.7 0.5 0 0.3). Given the documents are represented as vectors."""

import numpy as np

doc1 = np.array([1.0, 0.5, 0.3, 0, 0, 0])
doc2 = np.array([0.5, 1.0, 0, 0, 0, 0])
doc3 = np.array([0, 1.0, 0.8, 0.7, 0, 0])
doc4 = np.array([0, 0.9, 1.0, 0.5, 0, 0])
doc5 = np.array([0, 0, 0, 1.0, 0, 1.0])
doc6 = np.array([0, 0, 0, 0, 0.7, 0])
doc7 = np.array([0.5, 0, 0.7, 0, 0, 0.9])
doc8 = np.array([0, 0.6, 0, 1.0, 0.3, 0.2])
A10 = np.array([ doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8 ])

q = np.array([0, 0, 0.7, 0.5, 0, 0.3])

rank_A10 = np.linalg.matrix_rank(A10)

for i in range (0, rank_A10):
    cos_sim = np.dot(A10[i], q) / (np.linalg.norm(A10[i]) * np.linalg.norm(q))
    print("Cosine Similairty [Doc" + str(i + 1) + " q] = ", round(cos_sim, 2))

pos = 0
nearest = np.dot(A10[0], q) / (np.linalg.norm(A10[i]) * np.linalg.norm(q))
for i in range (1, rank_A10):
  temp = np.dot(A10[i], q) / (np.linalg.norm(A10[i]) * np.linalg.norm(q))
  if (nearest < temp):
    nearest = temp
    pos = i

print()

print("Document is the nearest with vector q: D" + str(pos + 1))