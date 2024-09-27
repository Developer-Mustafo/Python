# 1
print("Foydalanuvchi kiritgan sonni 2 lik sanoq sistemasiga aylantiring")
number2 = int(input("Sonni kiriting: "))
nm2 = ""
while number2 > 0:
    nm2 = str(number2 % 2) + nm2
    number2 //= 2
print(nm2)
# 2
print("Foydalanuvchi kiritgan sonni 8 lik sanoq sistemasiga aylantiring")
number8 = int(input("Sonni kiriting: "))
nm8 = ""
while number8 > 0:
    nm8 = str(number8 % 8) + nm8
    number8 //= 8
print(nm8)
