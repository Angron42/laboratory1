def checkPerfect(number):
    sum = 0
    for i in range(number - 1):
        if number % (i + 1) == 0:
            sum += i + 1
    return sum == number

number = int( input('Введите число >> ') )
isPerfect = checkPerfect(number)

print('Ваше число', 'досконале' if isPerfect else 'не досконале')