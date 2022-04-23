#%% MEGFP
import numpy as np

def megfp(A, b):
	n = np.shape(A)[0]
	for k in range(0, n - 1):
		for i in range(k + 1, n):
			m = A[i][k] / A[k][k]
			b[i][0] -= m * b[k][0]
			for j in range(k + 1, n):
				A[i][j] -= m * A[k][j]
			A[i][k] = 0
	return (A, b)

def megpp(A, b):
	n = np.shape(A)[0]

	for k in range(0, n - 1):
		l = max(list(zip(map(abs, A[k:, k]), range(k, n))))[1]

		if k != l:
			aux = np.copy(A[k])
			A[k] = np.copy(A[l])
			A[l] = aux
			aux = np.copy(b[k])
			b[k] = np.copy(b[l])
			b[l] = aux
		for i in range(k + 1, n):
			m = A[i][k] / A[k][k]
			b[i][0] -= m * b[k][0]
			for j in range(k + 1, n):
				A[i][j] -= m * A[k][j]
			A[i][k] = 0
	return (A, b)

def megpps(A, b):
	n = np.shape(A)[0]
	for k in range(0, n - 1):
		_a = []
		for i in range(k, n):
			s = max(list(map(abs, A[i, k:])))
			if(s != 0):
				_a.append((A[i][k] / s, i))
		l = max(_a)[1]

		if k != l:
			aux = np.copy(A[k])
			A[k] = np.copy(A[l])
			A[l] = aux
			aux = np.copy(b[k])
			b[k] = np.copy(b[l])
			b[l] = aux

		for i in range(k + 1, n):
			m = A[i][k] / A[k][k]
			b[i][0] -= m * b[k][0]
			for j in range(k + 1, n):
				A[i][j] -= m * A[k][j]
			A[i][k] = 0
	return (A, b)


def maxAbsA(A):
	(nl, nc) = np.shape(A)
	max_abs = np.amax(np.abs(A))
	for i in range(0, nl):
		for j in range(0, nc):
			if abs(A[i][j]) == max_abs:
				return i, j


def swap_lines(A, l1, l2):
	A[[l1, l2], :] = A[[l2, l1], :]

def swap_cols(A, c1, c2):
	A[:, [c1, c2]] = A[:, [c2, c1]]

def swap_elem(A, i1, i2):
	aux = A[i1]
	A[i1] = A[i2]
	A[i2] = aux

def megpt(A, b):
	n = np.shape(A)[0]
	var_order = list(range(0, n))

	for k in range(0, n - 1):
		(nl, nm) = maxAbsA(A[k:, k:])
		nl += k - 1
		nm += k - 1
		if k < nl:
			swap_lines(A, k, nl)
			swap_lines(b, k, nl)
		if k < nm:
			swap_cols(A, k, nm)
			swap_elem(var_order, k, nm)


		for i in range(k + 1, n):
			m = A[i][k] / A[k][k]
			b[i][0] -= m * b[k][0]
			for j in range(k + 1, n):
				A[i][j] -= m * A[k][j]
			A[i][k] = 0
	return (A, b, var_order)

A = [
	[1, 2, 3],
	[2, 6, 6],
	[1, 6, 10]
]

b = [
	[6],
	[14],
	[17]
]

A, b = np.array(A).astype(float), np.array(b).astype(float)
print(A)

print(megfp(np.copy(A), np.copy(b)))
print(megpp(np.copy(A), np.copy(b)))
print(megpps(np.copy(A), np.copy(b)))
print(megpt(np.copy(A), np.copy(b)))



