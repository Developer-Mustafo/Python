# 1
print('1 - factorial')
n = int(input("Son kiriting: "))
factorial = 0
for i in range(1, n + 1):
    if factorial == 0:
        factorial = 1
    factorial = factorial * i
print(f'{n} ning factoriali {factorial}')

# 2
print('2 - teskari')
number = input("Son kiriting: ")
reverse = ""
for i in range(len(number) - 1, -1, -1):
    reverse += number[i]
print(reverse)
# 3
print('3 - sonning raqamlar yig\'indisi')
num = input("Son kiriting: ")
total = 0
for i in range(0, len(num)):
    total += int(num[i])
print(f'{num}ning raqamlar yig\'indisi {total}')

# 4
print('4 - sonning raqamlar yig\'indisi songa tengmi ?')
nmr = int(input("Son kiriting: "))
son = 0
for i in range(1, nmr):
    if nmr % i == 0:
        son = son+i
print(nmr == son)
