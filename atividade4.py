prod= 60
pago= float(input("digite o valor pago: "))
if pago >= prod:
    troco= pago - prod
    print("seu troco é", troco)
else:
    print("valor insuficiente")