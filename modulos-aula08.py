# importa toda biblioteca
import math

num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {}'.format(num, raiz))





# importa só a parte especifica pedida, no caso a raiz quadrada
from math import sqrt, floor

num = int(input('digite um numero: '))
raiz = sqrt(num)
print('a raiz de {} é igual a {}'.format(num, floor(raiz))