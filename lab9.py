#%% Lab 9
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

#Rezolvare

A = np.array([
	[0.1, 0.1],
	[0.17, 0.11],
	[2.02, 1.29]
]).astype(float)

x = np.array([-5, -3.4, -2, -0.8, 0,1.2,2.5,4, 5,7,8.5])
y = np.array([4.4,4.5,4,3.6,3.9,3.8,3.5,2.5,1.2,0.5, 0.2])[np.newaxis]

A = np.pad(x[np.newaxis].T, ((0,0),(0,1)), 'constant', constant_values=(0,1)).astype(float)

_b = A.T @ y

L = cholesky(A.T @ A)

print(A@A.T)
print(L)
print(L@L.T)

#Pasul 1: L @ _y = _b

_y = l_solve(L, _b)
_y = np.array(_y)[np.newaxis].T

#Pasul 2: L.T @ _x = y

_x = u_solve(L.T, _y)


# linear regression
def lr_coef(x, y):
	n = np.size(x)
	(m_x, m_y) = (np.mean(x), np.mean(y))
	q = n * m_x * m_y
	(SS_xy, SS_xx) = (np.sum(y*x) - q, np.sum(x*x) - q)
	return (
		SS_xy / SS_xx,
		m_y - (SS_xy / SS_xx) * m_x
	)

