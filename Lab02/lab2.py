# -*- coding: utf-8 -*-
"""Lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GEEP68X-YnjuO_sHIe_XxcJ3Prdjjwyf

Exercise 1: Write a command to create vectors and get the number of elements in each vector. x = (1 3 5 2 9) and y = (−1 3 15 27 29)
"""

import numpy as np

x = [1,3,5,2,9]
y = [-1,3,15,27,29]

print("Số phần tử của vector x là", len(x))
print("Số phần tử của vector y là", len(y))

# Duyệt từng phần tử trong vector

for i in range(0, len(x), 1):
  print(i, x[i])

z = []
j = 0
for i in range(0, len(y), 1):
  if (y[i] > 0):
    z.insert(j,y[i])
    j += 1
print("vector z =", z)

"""Exercise 2: Write a command to create the following vectors with n elements (user-defined variable)"""

import math
import numpy as np

b = []
c = []
x = []
y = []
z = []
w = []
d = []
e = []
a = []
m = []
p = []


n = 10

# a)
for i in range(0, n):
  b.insert(i, 12 + 2*i)
print("vector b =", b)

# b)
for i in range(0, n):
  c.insert(i, 31 + 2*i)
print("vector c =", c)

# * c) 
for i in range(0, n + 1):
  if i < (n + 1) / 2:
    x.append(-n // 2 + i) # "//" chia lấy nguyên
  else:
    x.append(-(n // 2 - i))
print("vector x =", x)

# * d)
for i in range(0, n + 1):
  if i < (n + 1) / 2:
    y.append(n // 2 - i) # "//" chia lấy nguyên
  else:
    y.append(-(-n // 2 + i))
print("vector y =", y)

n = 8

# e)
for i in range(0, n):
  z.insert(i, 10 - 2*i)
print("vector z =", z) 

n = 10

# f)
for i in range(0, n):
  w.insert(i, 1 / pow(2,i)) 
print("vector w =", w) 

# g)
def fibonacci(n):
  if(n == 0 or n == 1):
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(0, n):
  d.insert(i, 1 / fibonacci(i)) 
print("vector d =", d) 

# h) 
def isPrime(n):
  if (n < 2):
    return False
  else:
    for i in range(2,n):
      if (n % i == 0):
        return False
    return True

count = 0
i = 0
j = 0
while(1):
  if(isPrime(i)):
    e.insert(j, 1 / i)
    j += 1
    count += 1
  i += 1
  if(count == n):
    break
print("vector e =", e)

# i) 
sum = 1
distance = 2
for i in range(0, n):
  a.insert(i, sum)
  sum += distance
  distance += 1 
print("vector a =", a) 

# * j)
for i in range(1, n, 1):
  m.append(1.0 / (i**2 + 1))
print("vector m =", m) 

# k)
for i in range(0, n):
  p.insert(i, i / (i+1)) 
print("vector p =", p) 

# l)
o = list(map(chr, range(97, 123)))
print("vector o =", o) 

# m)
temp = list(map(chr, range(97 - 32, 123 - 32)))
s = []
j = 0
for i in range (0,len(temp),3):
  s.insert(j, temp[i])
  j += 1
print("vector s =", s)

"""Exercise 3: Write a command to create the following vector by logarithmic spacing method"""

import numpy as np
n = 10
x = np.logspace(1, n, 10)
print(x)

"""Exercise 4: Let two vectors x = (1 2 3) and y = (98 12 33). Write a command to create a vector z = (1 2 3 98 12 33) from x and y."""

import numpy as np
x = [1,2,3]
y = [98,12,33]
z = np.array(x + y)
print("vector x =", x)
print("vector y =", y)
print("vector z =", z)

"""Exercise 5: Let two vectors x = (1 2 3) and y = (4 5 6). Write a command to create a vector"""

import numpy as np
x = [1,2,3]
y = [4,5,6]
z = np.array(x + y)

print("vector z =", z.reshape(2,3))

"""Exercise 6: Let x = (0 2 4 6 8 10 12 14 16 18 20). Write a command to perform the following:"""

import numpy as np
x = [0,2,4,6,8,10,12,14,16,18,20]

a = []
for i in range(0, 6, 1):
  a.append(x[i])
print("vector a =", a)

b = []
for i in range(len(x) - 5, len(x), 1):
  b.append(x[i])
print("vector b =", b)

c = []
c.extend([x[0], x[3], x[len(x)-1]])
print("vector c =", c)

d = []
for i in range (0,7,2):
  d.append(x[i])
print("vector d =", d)

e = []
for i in range (0, len(x), 1):
  if (i % 2 != 0):
    e.append(x[i])
print("vector e =", e)

f = []
for i in range (0, len(x), 1):
  if (i % 2 == 0):
    f.append(x[i])
print("vector f =", f)

"""Exercise 7: Let x = (3 11 −9 −131 −1 1 −11 91 −6 407 −12 −11 12 153 371)"""

import numpy as np
import math
x = [3,11,-9,-131,-1,1,-11,91,-6,407,-12,-11,12,153,371]

# (a) Find the maximize in the vector x
def findMaxInVector(x):
  max = x[0]
  for i in range(1, len(x), 1):
    if (x[i] > max):
      max = x[i]
  return max
print("a) The maximize in the vector x is", findMaxInVector(x))

# (b) Find the minimize in the vector x
def findMinInVector(x):
  min = x[0]
  for i in range(1, len(x), 1):
    if (x[i] < min):
      min = x[i]
  return min
print("b) The minimize in the vector x is", findMinInVector(x))

# (c) Find the index of the values of x that are greater than 10
def findListIndexOfValueGreatThan10(x):
  listIndex = []
  for i in range(0, len(x), 1):
    if (x[i] > 10):
      listIndex.append(i)
  return listIndex
print("c) The index of the values of x that are greater than 10", findListIndexOfValueGreatThan10(x))

# (d) Write command to reverse x vector
def reverseVector(x):
  reverseList = []
  for i in range(0, int(len(x) / 2), 1):
    temp = x[i]
    x[i] = x[len(x) - 1 - i]
    x[len(x) - 1 - i] = temp

  for i in range(0, len(x), 1):
    reverseList.append(x[i])
  
  return reverseList

print("d) Reverse x vector", reverseVector(x))

# (e) Write command to sort x vector in ascending order
def ascendingSort(x):
  x.sort()
  return x

print("e) Sort x vector in ascending order:", ascendingSort(x))

# (f) Write command to sort x vector in descending order
def descendingSort(x):
  for i in range(0, len(x) - 1, 1):
    for j in range(i + 1, len(x), 1):
      if (x[i] < x[j]):
        temp = x[i]
        x[i] = x[j]
        x[j] = temp
  return x

print("f) Sort x vector in descending order:", descendingSort(x))

# (g) Write command to count how many times have that x[i] + x[j] = 0,(i != j)
def countTimeThatExpressionTrue(x):
  count = 0
  for i in range(0, len(x) - 1, 1):
    for j in range(i + 1, len(x), 1):
      if (x[i] + x[j] == 0):
        count += 1
  return count

print("g) x[i] + x[j] = 0 appear " + str(countTimeThatExpressionTrue(x)) + " times")

# (h) Write command to count total number of duplicate elements in x vector
def countDuplicateElements(x):
  count = 0
  for i in range(0, len(x) - 1, 1):
    for j in range(i + 1, len(x), 1):
      if (x[i] == x[j]):
        count += 1
  return count

print("h) The total number of duplicate elements in x vector:", countDuplicateElements(x))

# (i) Write command to create a new y vector which yi = x[i] + x[n−i−1], where n is the length of x vector
def createNewVectorSatisfyRequirement(x):
  y = []
  if (len(x) % 2 != 0):
    for i in range(0, int(len(x) / 2) + 1, 1):
      y.append(x[i] + x[len(x) - 1 - i])
  else:
    for i in range(0, int(len(x) / 2), 1):
      y.append(x[i] + x[len(x) - 1 - i])
  return y

print("i) Vector y:", createNewVectorSatisfyRequirement(x))

# (j) Write command to create a new w vector which contains Armstrong/ Narcissistic numbers in x vector.
def countDigit(num):
  count = 0
  while (num > 0):
    num /= 10
    num = int(num)
    count += 1
  return count

def isArmstrongNum(num):
  temp = num
  count = countDigit(num)
  armstrongNum = 0
  while (temp > 0):
    lastDigit = int(temp) % 10
    armstrongNum += lastDigit**count
    temp /= 10
    temp = int(temp)
  if (num == armstrongNum):
    return True
  return False

def createVectorContainArmstrongNum(x):
  w = []
  for i in range(0, len(x), 1):
    if (isArmstrongNum(x[i])):
      w.append(x[i])
  return w

print("j) Vector contains Armstrong numbers in x vector:", createVectorContainArmstrongNum(x))
  
# (k) Write command to delete all negative numbers in x vector
def deleteNegativeNum(x):
  x.sort()
  count = 0
  for i in range (0, len(x), 1):
    if (x[i] < 0):
      count += 1

  for i in range (count - 1, -1, -1):
    x.pop(i)
  return x

print("k) Delete all negative numbers in x vector:", deleteNegativeNum(x))

x = [3,11,-9,-131,-1,1,-11,91,-6,407,-12,-11,12,153,371]

# (l) Write command to find median value in x vector
def findMedianValue(x):
  x.sort()
  return x[int(len(x) / 2)]

print("l) The median value in x vector", findMedianValue(x))

# (m) Write command to calculate the sum of all values which are less than mean value in x vector
def calSumValuesLessThanMeanValue(x):
  sum = 0
  for i in range (0, len(x), 1):
    sum += x[i]
  meanValue = float(sum) / len(x)

  sumOfValueLessThanMeanValue = 0
  for i in range (0, len(x), 1):
    if (x[i] < meanValue):
      sumOfValueLessThanMeanValue += x[i]
  return sumOfValueLessThanMeanValue

print("m) Sum of all values which are less than mean value in x vector =", calSumValuesLessThanMeanValue(x))

# (n) Write command to create a new vector which each negative value is replaced by its absolute value
def createVectorWithAbsoluteValue(x):
  listOfAbsoluteValue = []
  for i in range (0, len(x), 1):
    x[i] = abs(x[i])
    listOfAbsoluteValue.append(x[i])
  return listOfAbsoluteValue

print("n) Vector which each negative value is replaced by its absolute value:", createVectorWithAbsoluteValue(x))