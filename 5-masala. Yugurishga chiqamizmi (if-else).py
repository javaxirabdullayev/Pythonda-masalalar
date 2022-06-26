# 5-masala. Yugurishga chiqamizmi? (if-else)

# Foydalanuvchi bir nechta savollarga javob beradi.

# 1. Havo harorati
# 2. Yomg’ir yog’yaptimi?
# 3. Zal ochiqmi?

# Shartlar:

# 1. Harorat 5 dan past va 30 dan baland bo’lsa, yugurishga chiqmaymiz.
# 2. 5 va 30 orasida bo’lsa, yugurishga chiqamiz.
#     1. Agar yomg’ir yog’ayotgan bo’lsa, faqat zal ochiqligida yugurishga chiqamiz.

# Dastur 1.
havo0 = int(input("Havo haroratini kirgizing: "))
if havo0<5 or havo0>30:
    print("Yugurishga chiqmaymiz.")
elif 5<havo0<30:
    print("Yugurishga chiqamiz.")

    
    
# Dastur 2.   
    
havo1 = input("Yomg'ir yog'yaptimi? (ha/yo'q): ").lower()
havo3 = input("Zal ochiqmi? (ha/yo'q): ").lower()
if havo1 == 'ha' and havo3 == 'ha':
    print("Yugurishga zalga chiqamiz.")
else:
    print("Uyda bo'lamiz")