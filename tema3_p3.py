import matplotlib.pyplot as plt

f = lambda x: x * (x + 2) - 3
f_der = lambda x: 2 * x + 2

num_upper_deriv = lambda x, h: (f(x + h) - f(x)) / h
num_lower_deriv = lambda x, h: (f(x) - f(x - h)) / h


def get_data_upper_deriv(val_x):
	arr_err = []
	arr_err_abs = []
	arr_x_ax = [x for x in range(1, 21)]
	print("Erori pentru derivata inferioara numerica: ")
	print("x =", val_x)
	for i in range(1, 21):
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
	arr_err = []
	arr_err_abs = []
	arr_x_ax = [x for x in range(1, 21)]
	print("Erori pentru derivata inferioara numerica: ")
	print("x =", val_x)
	for i in range(1, 21):
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

ax2.legend(["eroare absoluta derivata superioara", "eroare absoluta derivata inferioara"], loc="upper right")
ax2.set_yscale('log', base = 10)
ax2.set(xlabel='h', ylabel='eroare absoluta',
	   title='Aproximarea derivatei')
ax2.grid()

fig2.savefig("err_abs.png")
plt.show()