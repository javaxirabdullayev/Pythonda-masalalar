# 3-masala. Parol biriktirish dasturi

# Masala. Foydalanuvchi parolni kiritadi. Agar parol uzunligi 8 dan kam bo’lsa, 
# “Parol kuchsiz, 8 ta yoki undan ko’p belgili bo’lishi kerak” xabari, bo’lmasa,
#  “Yangi parol saqlandi” xabari chiqariladi.


# Dastur:
    
parol = input("Parolni kiriting: ")
uzunlik = len(parol)
if uzunlik >= 8:
    print("Yangi parol saqlandi.")
else:
    print("Parol kuchsiz, 8 ta yoki undan ko’p belgili bo’lishi kerak")        