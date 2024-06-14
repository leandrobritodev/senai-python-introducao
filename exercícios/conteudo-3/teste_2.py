from random import randint

resultado_1 = 0
resultado_2 = 0
resultado_3 = 0
resultado_4 = 0
resultado_5 = 0
resultado_6 = 0

for i in range(1000):
    dado = randint(1,  6)

    if dado == 1:
        resultado_1 += 1
    elif dado == 2:
        resultado_2 += 1
    elif dado == 3:
        resultado_3 += 1
    elif dado == 4:
        resultado_4 += 1
    elif dado == 5:
        resultado_5 += 1
    elif dado == 6:
        resultado_6 += 1

print('1: ' + str(resultado_1))
print('2: ' + str(resultado_2))
print('3: ' + str(resultado_3))
print('4: ' + str(resultado_4))
print('5: ' + str(resultado_5))
print('6: ' + str(resultado_6))
