#chinese remainder theorem

modulos = [5, 11, 17]
a = [2, 3, 5]

#compute N
N = 1
for i in range(len(modulos)):
    N = N*modulos[i]

#compute y
y = []
for i in range (len(modulos)):
    y.append(int(N/modulos[i]))

#compute z
z = []
for i in range(len(modulos)):
    z.append(pow(y[i], -1, modulos[i]))

#compute x
x = 0
for i in range(len(modulos)):
    x = x + a[i]*y[i]*z[i]

print("x mod N = ", x%N)