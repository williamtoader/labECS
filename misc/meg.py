#%%
import numpy as np


def megpp(A, b, ok=True):
	n = np.shape(A)[0]
	if (np.shape(A)[0] != np.shape(A)[1]):
		raise ValueError("Matricea nu e pătratică!")
	elif b.size != np.shape(A)[0] and np.shape(b)[1] == 1:
		raise ValueError("Valori incompatibile între" + " A & b.", b.size, np.shape(A)[0])
	else:
		for k in range(n - 1):
			if ok:
				maxindex = np.abs(A[k:, k]).argmax() + k
				if A[maxindex, k] == 0:
					raise ValueError("Matricea nu e inversabilă!")
				if maxindex != k:
					A[[k, maxindex]] = A[[maxindex, k]]
					b[[k, maxindex]] = b[[maxindex, k]]
			else:
				if A[k, k] == 0:
					raise ValueError("Pivotul este nul!")
			for i in range(k + 1, n):
				m = A[i, k] / A[k, k]
				A[i, k:] = A[i, k:] - m * A[k, k:]
				b[i] = b[i] - m * b[k]
				A[i, k] = 0
		x = np.zeros_like(b, dtype=np.double)
		for j in range(n - 1, -1, -1):
			x[j] = (b[j] - np.dot(A[j, j + 1:], x[j + 1:])) / A[j, j]

		return A




A = np.array([[0., 2., 3.], [5., 6., 2.], [0., 6., 1.]])
b = np.array([[6.], [1.], [4.]])
print(megpp(A, b))