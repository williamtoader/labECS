# %%
f = lambda x: x * (x + 2) - 3
f_der = lambda x: 2 * x + 2

num_deriv = lambda x, h: (f(x + h) - f(x)) / h

val_x = 2
arr_err = []
arr_x_ax = range(1, 21)
print("x este", val_x)
for i in range(1, 21):
	h = 10 ** (-i)
	val_der = f_der(val_x)
	val_num_der = num_deriv(val_x, h)
	err_abs = abs(val_num_der - val_der)
	err_rel = err_abs / abs(val_der)
	arr_err.append(err_rel)

	print("h: %.1e, d: %.10f, nd: %.10f, ea: %.4e, er: %.4e" % \
		  (h, val_der, val_num_der, err_abs, err_rel))

# %%
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
# t = np.arange(0, 8, 0.00001)
# s = num_deriv(t,1)
# s_1_2 = num_deriv(t,0.5)
# s2 = f_der(t)

t = np.array(arr_x_ax)
s = np.array(arr_err)

fig, ax = plt.subplots()
ax.plot(t, s, label="nd-1")
# ax.plot(t, s_1_2, label="nd-2")
# ax.plot(t, s2, label="der")
ax.legend(["err rel"], loc="upper right")
ax.set(xlabel='x', ylabel='y',
	   title='Aproximarea derivatei')
ax.grid()

fig.savefig("test.png")
plt.show()

# %% Prob 2
## Tema 3,4
import matplotlib.pyplot as plt
import numpy as np


f = lambda x: x * (x + 2) - 3
f_der = lambda x: 2 * x + 2

num_upper_deriv = lambda x, h: (f(x + h) - f(x)) / h
num_lower_deriv = lambda x, h: (f(x) - f(x - h)) / h


def get_data_upper_deriv(val_x):
	global f, f_der, num_upper_deriv, num_lower_deriv
	arr_err = []
	arr_err_abs = []
	arr_x_ax = range(1, 21)
	print("Erori pentru derivata inferioara numerica: ")
	print("x =", val_x)
	for i in arr_x_ax:
		h = 10 ** (-i)
		val_der = f_der(val_x)
		val_num_der = num_upper_deriv(val_x, h)
		err_abs = abs(val_num_der - val_der)
		err_rel = err_abs / abs(val_der)
		arr_err.append(err_rel)
		arr_err_abs.append(err_abs)
		print("h: %.1e, d: %.10f, nd: %.10f, ea: %.4e, er: %.4e" % \
			  (h, val_der, val_num_der, err_abs, err_rel))
	return (arr_x_ax, arr_err, arr_err_abs)

def get_data_lower_deriv(val_x):
	global f, f_der, num_upper_deriv, num_lower_deriv
	arr_err = []
	arr_err_abs = []
	arr_x_ax = range(1, 21)
	print("Erori pentru derivata inferioara numerica: ")
	print("x =", val_x)
	for i in arr_x_ax:
		h = 10 ** (-i)
		val_der = f_der(val_x)
		val_num_der = num_lower_deriv(val_x, h)
		err_abs = abs(val_num_der - val_der)
		err_rel = err_abs / abs(val_der)
		arr_err.append(err_rel)
		arr_err_abs.append(err_abs)
		print("h: %.1e, d: %.10f, nd: %.10f, ea: %.4e, er: %.4e" % \
			  (h, val_der, val_num_der, err_abs, err_rel))
	return (arr_x_ax, arr_err, arr_err_abs)

ud_data = get_data_upper_deriv(2)
ld_data = get_data_lower_deriv(2)


fig, ax = plt.subplots()
ax.plot(ud_data[0], ud_data[1], label="derivata superioara")
ax.plot(ld_data[0], ld_data[1], label="derivata inferioara")

ax.legend(["eroare relativa derivata superioara","eroare relativa derivata inferioara"], loc="upper right")
ax.set_yscale('log', base = 10)
ax.set(xlabel='h', ylabel='eroare relativa',
	   title='Aproximarea derivatei')
ax.grid()

fig.savefig("err_rel.png")

fig2, ax2 = plt.subplots()
ax2.plot(ud_data[0], ud_data[2], label="derivata superioara")
ax2.plot(ld_data[0], ld_data[2], label="derivata inferioara")

ax2.legend(["eroare absoluta derivata superioara","eroare absoluta derivata inferioara"], loc="upper right")
ax2.set_yscale('log', base = 10)
ax2.set(xlabel='h', ylabel='eroare absoluta',
	   title='Aproximarea derivatei')
ax2.grid()

fig2.savefig("err_abs.png")
plt.show()

#%%
import math
def get_machine_epsilon():
	epsilon = 1
	while (epsilon + 1 > 1):
		epsilon = epsilon / 2
	return epsilon

def calc_serie(x):
	s = 1
	term = 1
	d = 1
	epsilon = get_machine_epsilon()
	while(abs(term) > epsilon):
		term *= x/d
		s += term
		d += 1
	e_to_x = math.e**x
	return (s, abs(s - e_to_x), abs((s - e_to_x)/e_to_x))


print("e: %.60f" % (math.e))
print("serie 1: %.60f,\nerr abs: %.10e, err rel: %.10e\n" % calc_serie(1))
print("e^10: %.60f" % (math.e**10))
print("serie 10: %.60f,\nerr abs: %.10e, err rel: %.10e\n" % calc_serie(10))
print("e^20: %.60f" % (math.e**20))
print("serie 20: %.60f,\nerr abs: %.10e, err rel: %.10e\n" % calc_serie(20))
print("e^-1: %.60f" % (math.e**-1))
print("serie -1: %.60f,\nerr abs: %.10e, err rel: %.10e\n" % calc_serie(-1))
print("e^-10: %.60f" % (math.e**-10))
print("serie -10: %.60f,\nerr abs: %.10e, err rel: %.10e\n" % calc_serie(-10))
print("e^-20: %.60f" % (math.e**-20))
print("serie -20: %.60f,\nerr abs: %.10e, err rel: %.10e\n" % calc_serie(-20))
