#%% EX 3:
import math


def get_machine_epsilon():
	epsilon = 1
	while epsilon + 1 > 1:
		epsilon = epsilon / 2
	return epsilon


def serie_cos(x):
	if x < 0 or x > math.pi:
		return
	cos_val = 1
	term = 1
	k = 1
	epsilon = get_machine_epsilon()
	while abs(term) > epsilon:
		term *= -1 * (x ** 2) / (k ** 2 + k)
		cos_val += term
		k += 2
	return cos_val


# print(serie_cos(math.pi / 3.0))

x = [0, math.pi / 6, math.pi / 4, math.pi / 3,
	 math.pi / 2, 2 * math.pi / 3,
	 3 * math.pi / 4, 5 * math.pi / 6, math.pi]

for val_x in x:
	data = (
		val_x,
		math.cos(val_x),
		serie_cos(val_x),
		abs(math.cos(val_x) - serie_cos(val_x)),
		abs(math.cos(val_x) - serie_cos(val_x)) /
		abs(math.cos(val_x))
	)
	print("x:\t%.20f, cos(x):\t%.20f, serie_cos(x):\t%.20f, err abs:\t%.4e, err rel:\t%.4e" % data)
