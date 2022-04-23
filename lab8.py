import numpy as np
import math

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