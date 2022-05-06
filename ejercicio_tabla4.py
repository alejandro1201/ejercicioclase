lista=[]
for x in range (20):
    valor=int(input('Ingrese un numero: '))
    lista.append(valor)
    if lista [x]<0:
        lista [x]=int(input('Por favor digite un numero positivo: '))
print(lista)        