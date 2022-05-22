import numpy as np
from scipy import linalg
# m >= n
# A inversabila la stanga


A = np.array([
	[1, -1, -4],
	[1, 4, -2],
	[1, 4, 2],
	[1, -1, 0]
]).astype(float)


test_qr = np.linalg.qr(A)

sign = lambda x: -1 if x < 0 else 1

def get_v_i(A, i):
	n = np.shape(A)[0]
	a_i = (A[:, i])[:,np.newaxis]
	norm_a_i = np.linalg.norm(a_i)
	e_i = np.array([1 if x == 0 else 0 for x in range(0, n)])[:, np.newaxis]
	v_i = a_i + sign(a_i[0]) * norm_a_i * e_i
	return v_i


def build_H_i(v, n):
	print((2 * (v.T @ v)) * (v @ v.T))
	return np.eye(n) - (2 * (v.T @ v)) * (v @ v.T)


H_l = []
m = np.shape(A)[1]
n = np.shape(A)[0]
R = np.copy(A)
Q = np.eye(n)
for i in range(0, m - 1):
	print()
	n = np.shape(A)[0]
	H = build_H_i(get_v_i(A, i), n)
	_H = np.pad(H, ((i,0),(i,0)))
	for j in range(0, i):
		_H[j][j] = 1

	R = _H @ R
	Q = Q @ _H

	A = (H @ A)[1:, 1:]
	print("A=", A)




# print(get_v_i(A, 1))

print("Q~=",Q)
print("R~=",R)

print("A = Q x R = ", Q @ R)

print("Q=",test_qr[0])
print("R=",test_qr[1])



