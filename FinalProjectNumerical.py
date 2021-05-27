'''
Max Scott
2020-2021 school year 
iterative proses to estimate igan value
NOTE: this project was done in colaboraton with two others who 
created the slidshow and provided the mathmatical proses.
The code was writen by miself and is below. 
'''

import numpy as np
    # finds largest number in matrix 
def findBig(mat,n):
  big = mat[0][0]
  for i in range(n):
    if( big < abs(mat[i][0])):
      big = mat[i][0]
  return(big)
    # normalizes the matrix 
def norm(mat,n):
  newMat = mat
  big = findBig(mat,n)
  for i in range(n):
    newMat[i][0] = mat[i][0] / big
  return newMat
# aproximats the igan value with many iterations 
def loop(mat, iterat, L):
    x0 = np.array([[1.0],[-2.0],[0.0],[3.0]])
    for i in range(iterat):
        x0 = np.matmul(mat,x0)
        print("igan val", findBig(x0,L) )
        x0 = norm(x0,L)    
    print(i, " iterations")
    print(x0)
    print("")
    print("")


# testing
A = np.array([[0.0,2.0], 
              [2.0,-3.0]])
print("the matrix is ")
print(A)
x0 = np.array([[1.0],
               [1.0]])
print("the original guess is")
print(x0)
print("")
print("")
x0 = np.matmul(A,x0)
x0 = norm(x0,2)
print("first iteration ")
print(x0)
print("")
print("")
x1 = np.matmul(A,x0)
x1 = norm(x1,2)
print("secont  iteration ")
print(x1)
print("")
print("")
x2 = np.matmul(A,x1)
x2 = norm(x2,2)
print("third iteration ")
print(x2)