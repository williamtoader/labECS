import numpy as np


def megfp(A, b):
	A = np.copy(A)
	b = np.copy(b)
	n = np.shape(A)[0]

	for k in range(0, n - 1):
		for i in range(k + 1, n):
			m = A[i][k] / A[k][k]
			b[i][0] -= m * b[k][0]
			for j in range(k + 1, n):
				A[i][j] -= m * A[k][j]
			A[i][k] = 0
	return A, b

def usolve(A, b):
	A = np.copy(A)
	b = np.copy(b)
	x = []
	n = np.shape(A)[0]

	for i in range(n - 1, -1, -1):
		x.append(
			((b[i] - np.dot(x, A[i, i + 1:])) /
			A[i][i])[0]
		)

	return list(reversed(x))

def lsolve(A, b):
	A = np.copy(A)
	b = np.copy(b)
	x = []
	n = np.shape(A)[0]

	for i in range(0, n):
		x.append(
			((b[i] - np.dot(x, A[i, :i])) / A[i][i])[0]
		)
	return x

def step_LU(A):
	n = np.shape(A)[0]
	L = np.zeros((n, n))
	U = np.zeros((n, n))

	U[0][0] = A[0][0]
	L[0][0] = 1

	for i in range(1, n):
		L[i][0] = A[i][0] / A[0][0]
		U[0][i] = A[0][i]

	S = A[1:, 1:] - (
		np.multiply(
			np.array([A[1: 0]]).T,
			np.array([A[0, 1:]])
		)
	) / A[0][0]
	return S, L, U