def t_next(t, l):
    return -t * (4 / l + 1)

suma = 0

eroare_relativa = 1

k = 1

target = 4**(-2)
t = -1

while eroare_relativa>10**(-9) :
    t = t_next(t, k)
    suma += t

    eroare_absoluta = abs(target-suma)
    eroare_relativa= abs(target-suma)/eroare_absoluta
    k+=1

    print(k,'\t',"%.12f"% suma,"%.12f"% target,"%.2f"%eroare_absoluta,"%.2f"%eroare_relativa,"n = ",n-1)
    print("cel mai mic n",n-1)