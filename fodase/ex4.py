def fibo(num: int):
    if num == 1 or num == 0:
        return num
 
    else:
        return fibo(num - 1) + fibo(num -2)

number = int(input())

print(fibo(number))