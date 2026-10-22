
#       Butun sonlar

# integer ---- 10 20 50 100 1111 5000
# float ----- 1.5 10.5 22.3
#
# int()
# float()

# son1 = 1000
# son2 = 10.5
#
# son1, son2, son3 = 1000 , 2.5 , 20
#
# print(son1+son2+son3)



#          Input
#
# a = int(input("Tug'ilgan kunizni kiriting: "))
# age = 2026 - a
# print(f"Sizning yoshingiz {age}")


# num = int(input(" Enter a number: "))
# result = num * num
# print(result)

# a =input("ismingizni kiriting: ")
# print(f"xush kelibsiz {a}")

# a = "Toshkent"
# b = 5
# print(a.lower())
# print(a.capitalize())



# a = input("Ismingiz nma: ")
# b = input("Familiyangiz nma: ")
# c = int(input("Yoshingiz nechida: "))
#
# print(f"{a} {b} {c}")

mevalar = ['olma','anor','behi','banan']

print(mevalar[3].upper())
print(mevalar[3])

# listni ichidagi qiymatni amlmashtirish

mevalar[3] = 'uzum'
print(mevalar)


# Ro'yxatdaga element qo'shish

mevalar.append('uzum')
print(mevalar)

# Ro'yxatga index bo'yicha element qo'shish

mevalar.insert(0,'olcha')
print(mevalar)

# Ro'yxatdan element o'chirish

del mevalar[3]
print(mevalar)
# nomi bo'yicha ro'yxatdan element o'chirish

mevalar.remove('olcha')
print(mevalar)

# Ro'yxatdan element sug'urib olish
meva = mevalar.pop(1)
print(meva)

