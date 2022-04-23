# Precizia mașinii
import numpy as np
import math
print(np.finfo(float).eps)
# 2.22044604925e-16

print(np.finfo(np.float32).eps)
# 1.19209e-07

f = lambda x: (math.sqrt(x+1)-math.sqrt(x))*x

g = lambda x: x/(math.sqrt(x+1)+math.sqrt(x))
op = lambda a,b,c: a * b / c

print("%.20f"%f(500), "%.20f"%g(500))
print("{:.20f}".format(f(500)))

print("%.20f"%f(500))
print()
#%%
h = lambda x: x*(x*(x-6.1)+3.2)+1.5
h2 = lambda x: (x*x*x)-(6.1*(x*x))+(3.2*x)+1.5
print("%.60f"%h(500), "%.60f"%h2(500))
print("%.60f"%((h(4.71)*1000-h2(4.71)*100)/1000))
print("%.60f"%(h(4.71)-h2(4.71)))

#%%
import math
import numpy as np
def f(a,b,c):
	delta = (b**4 -(4*a*c)**2)/((b**2)+(4*a*c))
	if(delta < 1):
		print("No real solutions")
		return
	elif(delta==0):
		print("Ec are o soluție %.20f"%(-(b/(2*a))))
	else:
		print(delta)
		sqrt_delta = np.sqrt(delta)
		print(sqrt_delta)
		root1 = (-b + sqrt_delta) / (2 * a) if b < 0 else (-b - sqrt_delta) / (2 * a)
		root1alt = (-b + sqrt_delta) / (2 * a) if b >= 0 else (-b - sqrt_delta) / (2 * a)
		root2 = (c / root1) if root1 > c else root1alt
		print("Sol1 %.20f" % (root1))
		print("Sol2 %.20f" % (root2))

f(1,2,0.01)
