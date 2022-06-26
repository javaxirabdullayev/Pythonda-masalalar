# 6-masala. Taklif qilingan yoki yo’q

# Dasturda to’yga chaqirilgan mehmonlar ro’yxati bor. Foydalanuvchi ismini yozadi.
# Agar chaqirilgan bo’lsa, “Keling, mehmon” xabari chiqadi va u mehmon ro’yxatdan
# olib tashlanadi. Agar chaqirilmagan mehmon bo’lsa, “O’g’il to’yga kelarsiz” xabari
# chiqariladi.

# Dastur.

royhat = ['sardor', 'temur', 'bobur', 'azamat', 'hasan', 'husan', 'olim', 'ali', 'vali']

ism = (input("Ismingizni kiriting: ")).lower()
if ism in royhat:
    print(f"{ism.title()}, xush kelibsiz!")
else:
    print(f"{ism.title()}, o’g’il to’yga kelarsiz!")