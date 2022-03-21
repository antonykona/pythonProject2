def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

try:
    x=int(input('Введите число для проверки:'))
    if is_prime(x) and x!=1:
        print('Число простое')
    else:
        print('Число непростое')
except:
    print('Ошибка ввода данных')
