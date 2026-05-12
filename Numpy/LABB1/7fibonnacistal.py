def fib(n):
    assert n>=0 
    if 0<=n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Value for n: "))
print(fib(n))