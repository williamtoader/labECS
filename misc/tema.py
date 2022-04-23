import numpy as np

A = [
	[2, -1, -2],
	[-4, 6, 3],
	[-4, -2, 8]
]


A = np.array(A).astype(float)
shapeA = np.shape(A)


def doolittleLU(A):
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


print(doolittleLU(A))
print(detUsingLU(doolittleLU(A)))
print(croutLU(A))
print(detUsingLU(croutLU(A)))