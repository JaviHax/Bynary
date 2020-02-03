'''
Este codigo convierte un los valores de un array al valor de una variable
debe subirse a github
'''

lista = [1,1,0,1]
exp = 0
val = 0
long  = len(lista)
lista.reverse()
for i in range(0, long):
    rec = lista[i] * (2**exp)
    val += rec
    exp += 1

print(val)