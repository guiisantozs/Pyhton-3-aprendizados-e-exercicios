a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando qual é o menor.
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
#Verificando qual é o maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
