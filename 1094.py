contador = 1 
listaR = []
listaS = []
listaC = []
x = int(input())

while contador <=x:
    a,b = input().split()
    a = int(a)
    b = str(b).lower()
    contador = contador + 1
    if b == "r":
        listaR.append(a)
    if b == "s":
        listaS.append(a)
    if b == "c":
        listaC.append(a)

calcTotal = (sum(listaR)+sum(listaS)+sum(listaC))
porcentC = (sum(listaC) / calcTotal)*100
porcentR = (sum(listaR) / calcTotal)*100
porcentS = (sum(listaS) / calcTotal)*100

print("Total: {} cobaias".format(calcTotal))
print("Total de coelhos: {}".format(sum(listaC)))
print("Total de ratos: {}".format(sum(listaR)))
print("Total de sapos: {}".format(sum(listaS)))
print("Percentual de coelhos: {:.2f} %".format(porcentC))
print("Percentual de ratos: {:.2f} %".format(porcentR))
print("Percentual de sapos: {:.2f} %".format(porcentS))


