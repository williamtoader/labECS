#%% Lab 10
import numpy as np
import math

def l_solve(A, b):
	A = np.copy(A)
	b = np.copy(b)
	m = np.shape(A)[0]
	x = []
	for i in range(0, m):
		x.append(
			((b[i] - np.dot(x, A[i, 0:i]))
			/ A[i][i])[0]
		)
	return x

def u_solve(A, b):
	A = np.copy(A)
	b = np.copy(b)
	m = np.shape(A)[0]
	x = []
	for i in range(m - 1, -1, -1):
		x.append(
			((b[i] - np.dot(x, A[i, i+1:]))
			/ A[i][i])[0]
		)
	x = list(reversed(x))
	return x

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

matrixList = [
	[
		[
			[0.10, 0.10],
			[0.17, 0.11],
			[2.02, 1.29]
		],
		[
			[0.26],
			[0.28],
			[3.31]
		]
	],
[
		[
			[0.10, 0.10],
			[0.17, 0.11],
			[2.02, 1.29]
		],
		[
			[0.27],
			[0.25],
			[3.33]
		]
	],
[
		[
			[1, -1],
			[0, 1e-10],
			[0, 0]
		],
		[
			[0],
			[1e-10],
			[1]
		]
	]
]

def xdet(A):
	d = np.linalg.det(A)
	return d if d > 1e-14 else 0

def solve(matrixList):
	c = 0
	for syst in matrixList:
		c += 1
		A = np.copy(np.array(syst[0])).astype(float)
		b = np.copy(np.array(syst[1])).astype(float)

		# checks
		if xdet(A.T @ A) == 0:
			print("err at ", str(c))
			continue
		if np.shape(A)[0] < np.shape(A)[1]:
			print("err at ", str(c))
			continue
		if np.shape(A)[0] != np.shape(b)[0]:
			print("err at ", str(c))
			continue

		_A = np.vstack(
			[
				np.block([np.eye(np.shape(A)[0]), 	A]),
				np.block([A.T, 						np.zeros((np.shape(A)[1], np.shape(A)[1]))])
			]
		)

		_b = np.vstack(
			[
				b,
				np.zeros(np.shape(A)[1])[:,np.newaxis]
			]
		)

		print("Solved %d " % c, str(megpps(_A, _b)))
A = np.array(matrixList[1][0])
b = np.array(matrixList[1][1])

solve(matrixList)

epsValList = [10**-i for i in range(0, 20)]
epsValSqrtList = [10**-i for i in range(0, 20)]

def generateMatrixList(epsVals):
	return [
		[
			np.array(
				[
					[1, 1, 1],
					[eps, 0, 0],
					[0, eps, 0],
					[0, 0, eps]
				]
			),
			np.array(
				[
					[1],
					[0],
					[0],
					[0]
				]
			)
		]
		for eps in epsVals
	]
print("Solving for normal epsilon")
solve(generateMatrixList(epsValList))

print("Solving for square root of epsilon")
solve(generateMatrixList(epsValSqrtList))
