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
