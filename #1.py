from numpy import sqrt

getResult = lambda m, n: ( sqrt(m) - sqrt(n) ) / m

m = int( input('Введите число m >> ') )
n = int( input('Введите число n >> ') )
z = getResult(m, n)

print('Результат', z)