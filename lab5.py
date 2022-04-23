#%%
import numpy as np

print("%.7e" % np.linalg.det([[3, 5, 3],[2, 2, 3],[-1, -3, 0]]))

def det(A):
	d = np.linalg.det(A)
	return d if abs(d) > 1e-14 else 0

#%%
import numpy as np
A = [[1,2,3],[4,5,6],[7,8,9]]

n = np.shape(A)[0]

b = np.array([[],[],[]])

def checkdets(A):
	n = np.shape(A)[0]
	for k in range(0, n):
		print(k)
		mat_colt = [l[k:n] for l in A[k:n]]
		print(mat_colt)
checkdets(A)
#

#


for k in range(1, n):
	for i in range(k + 1, n + 1):
		m =  A[i][k] / A[k][k]
		b[i] = b[i] - m * b[k]


#%%
import numpy as np
A = [[1,2,3],[4,5,6],[7,8,9]]

n = np.shape(A)[0]

b = np.array([[],[],[]])
def checkdets(A):
	n = np.shape(A)[0]
	for k in range(0, n):
		mat_colt = [l[k:n] for l in A[k:n]]
		print(mat_colt)
		if(det(mat_colt) == 0):
			return False
	return True
checkdets(A)