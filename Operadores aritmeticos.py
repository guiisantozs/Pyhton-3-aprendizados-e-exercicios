n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
rd = n1 % n2
print('A soma vale {}, \n a multiplicação vale {}, \n e a divisão vale {:.3f}!'.format(s,m,d), end='')
print('A divisão inteira é {}, a exponênciação é {}, e o resto da divisão é {}!'.format(di,p,rd))
