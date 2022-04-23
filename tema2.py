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

print("%.65f" % sum)