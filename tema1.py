# %% Tema 1
import math

calc_sold = lambda t, c, d, n: \
	c * ((1 + d / n) ** (n * t))
solve_t = lambda s, c, d, n: \
	math.log(s / c, (1 + d / n)) / n

result_a = calc_sold(17, 5000, 0.85, 1)
print(result_a)

result_b = solve_t(result_a, 5000, 0.85, 12)
print(result_b)

print("%d ani, %d luni" %
	(result_b, (result_b - math.floor(result_b)) * 12))
