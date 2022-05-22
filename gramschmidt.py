#%%
# Verificam A matrice m x n cu m >= n
# Verificam A matrice inversabila la stanga

import numpy as np
import scipy.linalg as scla

# Gram Schmidt clasic

def gsc(A):
	A = np.copy(A)
	(m, n) = np.shape(A)
	R = np.zeros((n, n))
	Q = np.empty((m, n))
	for j in range(0, n):
		v = A[:, j]
		for i in range(0, j):
			R[i][j] = np.dot(Q[:, i], A[:, j])
			v = v - (R[i][j] * Q[:, i])
		R[j][j] = np.linalg.norm(v[j])
		Q[:, j] = v / R[j][j]
	return Q, R


# Gram Schmidt modificat
def gsm(A):
	A = np.copy(A)
	(m, n) = np.shape(A)
	R = np.zeros((n, n))
	Q = np.empty((m, n))
	v = np.empty((m, n))
	for j in range(0, n):
		v[:, j] = a[:, j]

	for j in range(0, n):
		R[j][j] = np.linalg.norm(v[:, j])
		Q[:, j] = v[:, j] / R[j][j]
		for i in range(j + 1, n):
			R[j][i] = np.dot(Q[:, j], v[:, i])
			v[:, i] = v[:, i] - (R[j][i] * Q[:, j])
	return Q, R

#Testam
A = [
	np.array([
		[1, -1],
		[0, 10**(-k)],
		[0, 0]
	])
	for k in range(1, 9)
]

for a in A:
	(Q, R) = gsc(a)
	print(Q, R)
	print("v1", Q.T @ Q,np.allclose(Q.T @ Q, np.eye(np.shape(a)[1])))
	print("v2", np.allclose(Q @ R, a))

A = [
	scla.hilbert(k)
	for k in range(2, 12)
]

for a in A:
	(Q, R) = gsm(a)
	print(Q, R)
	print("v1", Q.T @ Q, np.allclose(Q.T @ Q, np.eye(np.shape(a)[1])))
	print("v2", np.allclose(Q @ R, a))