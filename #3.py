from random import randint

def getMinNumber(array):
    length = len(array)
    minNumber = array[0]

    for i in range(length):
        number = array[i]
        if number < minNumber:
            minNumber = number

    return minNumber

def getProduct(array):
    length = len(array)
    product = 1

    for i in range(length):
        number = array[i]
        if not number == 0:
            product *= number

    return product

def printOddReversed(array):
    length = len(array)
    for i in range(length):
        i = length - i - 1
        number = array[i]

        if number >= 0:
            print(number)

array  = []
length = int( input('Введіть розмір масиву >> ') )

for i in range(length):
    randomNumber = randint(-10, 10)
    array.append(randomNumber)

print('Масив', array)
print('Мінімальний елемент масиву', getMinNumber(array))
print('Добуток ненульових елементів масиву', getProduct(array))
print('Додатні елементи масиву у зворотньому')
printOddReversed(array)