#%%
epsilon = 1
last = 0
while(epsilon + 1 > 1):
    last = epsilon
    epsilon = epsilon / 2


print(last)
print("%.60f" % last)
print("%.60f" % epsilon)
print("%.60f" % 0)

#%%

for n in range(1, 11):
    x = 1/n
    print("n:", n)
    print("x:", "%.16f" % x)
    for j in range(1, 31):
        x = (((n+1)*x)-1)
        if (j % 10 == 0):
            print(j, "%.16f" % x)
    print()

#%% Ex 5
epsilon = 1
last = 0
while(epsilon + 1 > 1):
    last = epsilon
    epsilon = epsilon / 2

term = 1
sum = 0
while(term > epsilon):
    sum += term
    term /= 3

print("%.20f" % sum)