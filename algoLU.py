#%% LU fara pivotare
import numpy as np
import math
A = [
	[2, -1, -2],
	[-4, 6, 3],
	[-4, -2, 8]
]


A = np.array(A).astype(float)
shapeA = np.shape(A)


def step(A):
	n = np.shape(A)[0]
	L = np.zeros(np.shape(A))
	U = np.zeros(np.shape(A))

	U[0][0] = A[0][0]
	L[0][0] = 1
	for i in range(1, n):
		L[i][0] = A[i][0] / A[0][0]
		U[0][i] = A[0][i]

	S = A[1:, 1:] - (np.multiply(np.array([A[1:, 0]]).T, np.array([A[0, 1:]]))) / A[0][0]
	return (S, L, U)

def lufp(A):
	A = np.copy(A)
	n = np.shape(A)[0]
	L = np.zeros(n)
	U = np.zeros(n)
	c = 0
	for i in range(0, n):
		(_S, _L, _U) = step(A)
		A = _S
		_L = np.pad(_L, ((i, 0), (i, 0)), 'constant')
		_U = np.pad(_U, ((i, 0), (i, 0)), 'constant')

		L = np.add(L,_L)
		U = np.add(U,_U)
	return (L, U)

def cholesky(A):
	A = np.copy(A)
	n = np.shape(A)[0]
	L = np.zeros(np.shape(A)).astype(float)

	for i in range(0, n):
		for k in range(0, i + 1):
			s = sum(
				L[i][j] * L[k][j] for j in range(0, k)
			)
			if i == k:
				L[i][i] = math.sqrt(A[i][i] - s)
			else:
				L[i][k] = 1.0 / L[k][k] * (A[i][k] - s)
	return L

def ldlt(A):
	L = cholesky(A)
	n = np.shape(A)[0]
	D = np.diag(A)
	for i in range(0, n):
		for j in range(0, n):
			L[i][j] = L[i][j] / D[i]
	return (L, D)

def dolittleLU(A):
	A = np.copy(A)
	n = np.shape(A)[0]
	L = np.zeros(np.shape(A))
	U = np.zeros(np.shape(A))

	for i in range(0, n):
		# Superior triunghulara
		for k in range(i, n):
			s = sum(L[i][j] * U[j][k] for j in range(0, i))
			U[i][k] = A[i][k] - s
		#Inferior triunghiulara
		for k in range(i, n):
			if i == k:
				L[i][i] = 1
			else:
				s = sum(L[k][j] * U[j][i] for j in range(0, i))
				L[k][i] = (A[k][i] - s) / U[i][i]
	return (L, U)

def croutLU(A):
	A = np.copy(A)
	n = np.shape(A)[0]
	L = np.zeros(np.shape(A))
	U = np.eye(n)

	for i in range(0, n):
		# Superior triunghulara
		for k in range(i, n):
			s = sum(L[k][j] * U[j][i] for j in range(0, i))
			L[k][i] = A[k][i] - s
		#Inferior triunghiulara
		for k in range(i, n):
			if i != k:
				s = sum(L[i][j] * U[j][k] for j in range(0, i))
				U[i][k] = (A[i][k] - s) / L[i][i]

	return (L, U)

A2 = np.array([[25,15,-5],[15,18, 0], [-5,0,11]]).astype(float)

def detUsingLU(luTuple):
	(L, U) = luTuple;
	return np.prod(np.diag(L)) * np.prod(np.diag(U))


print(dolittleLU(A))
print(detUsingLU(dolittleLU(A)))
print(croutLU(A))
print(detUsingLU(croutLU(A)))
