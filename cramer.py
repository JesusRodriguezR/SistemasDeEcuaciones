import numpy as np
import sys

n = int(input('Enter number of unknowns:'))

a = np.zeros((n,n+1))



x = np.zeros(n)

print('Enter Augmented Matrix Coefficients:')
for i in range(n):
	for j in range(n+1):
		a[i][j] = float(input('a['+str(i)+']['+str(j)+']='))
print ("Ax = b: \n",a)

A = np.zeros((n,n))
for i in range(n):
	for j in range(n):
		A[i][j]=a[i][j]

D = np.linalg.det(A)

for k in range(0,n):
	Ax = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if j == k:
				Ax[i][j] = a[i][n]
			else:
				Ax[i][j] = a[i][j]
	Dx = np.linalg.det(Ax)
	x = Dx/D
	print("x"+str(k)+": \n",x)
