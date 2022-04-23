#%%
import operator

import numpy as np

print(np.shape([[0,1,2],[5,6,7]]))

#%% Substitutie descendenta


def check_shape_1(A, b):
	if np.shape(A)[0] != np.shape(A)[1]:
		return False
	if (not np.allclose(A, np.tril(A))):
		return False
	if np.linalg.det(A) == 0:
		return False
	if (not (np.shape(A)[0] == np.shape(b)[0]) and (np.shape(b)[1] == 1)):
		return False
	return True


L = []
L.append((
	np.array([
		[2, 0, 0],
		[-1, 4, 0]
	]).astype(float),
	np.array([
		[2],
		[3]
	]).astype(float)
))
L.append((
	np.array([
		[2, 1, 0],
		[-1, 4, 0],
		[2, 4, 1]
	]).astype(float),
	np.array([
		[2],
		[3],
		[3]
	]).astype(float)
))
L.append((
	np.array([
		[2, 0, 0],
		[-1, 4, 0],
		[-2, 4, 1]
	]).astype(float),
	np.array([
		[2],
		[3]
	]).astype(float)
))
L.append((
	np.array([
		[2, 0, 0],
		[-1, 0, 0],
		[-2, 4, 1]
	]).astype(float),
	np.array([
		[2],
		[3],
		[3]
	]).astype(float)
))
L.append((
	np.array([
		[2, 0, 0],
		[-1, 4, 0],
		[-2, 4, 1]
	]).astype(float),
	np.array([
		[2],
		[3],
		[3]
	]).astype(float)
))

comb_lin = lambda A, B: sum(list(map(lambda a: a[0]*a[1], list(zip(A, B)))))
print(comb_lin([0,2,4],[5,3,1]))
x = []
c = 0
for sys in L:
	c+=1
	A = sys[0]
	b = sys[1]
	(m, n) = np.shape(A)
	if(check_shape_1(A, b)):
		print("Matrice ok!", c)

		for i in range(0, m):
			x.append(
				(b[i] - comb_lin(x, A[i][0:i] if i > 0 else []))
				/ A[i][i]
			)
		print(list(map(float, x)))

#%% Substitutie ascendenta


def check_shape_1(A, b):
	# Matrice inferior triunghiulara
	if np.shape(A)[0] != np.shape(A)[1]:
		return False
	if (not np.allclose(A, np.tril(A))):
		return False
	if np.linalg.det(A) == 0:
		return False
	if (not (np.shape(A)[0] == np.shape(b)[0]) and (np.shape(b)[1] == 1)):
		return False
	return True


def check_shape_2(A, b):
	#Matrice superior triunghiulara
	if np.shape(A)[0] != np.shape(A)[1]:
		return False
	if (not np.allclose(A, np.triu(A))):
		return False
	if np.linalg.det(A) == 0:
		return False
	if (not (np.shape(A)[0] == np.shape(b)[0]) and (np.shape(b)[1] == 1)):
		return False
	return True


U = []
# a
U.append([
	np.array([
		[2, -1, 2],
		[0, 4, 4]
	]).astype(float),
	np.array([
		[-1],
		[8]
	]).astype(float)
])
# b
U.append([
	np.array([
		[2, -1, -2],
		[0, 4, 4],
		[1, 0, 1]
	]).astype(float),
	np.array([
		[-1],
		[8],
		[1]
	]).astype(float)
])
# c
U.append([
	np.array([
		[2, -1, -2],
		[0, 4, 4],
		[0, 0, 1]
	]).astype(float),
	np.array([
		[-1],
		[8]
	]).astype(float)
])
# d
U.append([
	np.array([
		[2, -1, -2],
		[0, 0, 4],
		[0, 0, 1]
	]).astype(float),
	np.array([
		[-1],
		[8],
		[1]
	]).astype(float)
])
# e
U.append([
	np.array([
		[2, -1, -2],
		[0, 4, 4],
		[0, 0, 1]
	]).astype(float),
	np.array([
		[-1],
		[8],
		[1]
	]).astype(float)
])

for sys in U:
	if(check_shape_2(sys[0], sys[1])):
		sys[0] = np.fliplr(np.flipud(sys[0]))
		sys[1] = np.flipud(sys[1])

comb_lin = lambda A, B: sum(list(map(lambda a: a[0]*a[1], list(zip(A, B)))))
x = []
c = 0
for sys in U:
	c+=1
	A = sys[0]
	b = sys[1]
	(m, n) = np.shape(A)
	if(check_shape_1(A, b)):
		print("Matrice ok!", c)

		for i in range(0, m):
			x.append(
				(b[i] - comb_lin(x, A[i][0:i] if i > 0 else []))
				/ A[i][i]
			)
		reversed(x)
		print(list(map(float, x)))