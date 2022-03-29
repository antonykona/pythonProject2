def fib(n):
    if n<1:
        return None
    if n<3:
        return 1
    return fib(n-2)+fib(n-1)
n=int(input())
if n>=0:
    print(fib(n))
else:
    print('try ')