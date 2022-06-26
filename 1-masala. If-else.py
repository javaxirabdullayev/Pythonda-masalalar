# 1-masala. If-else

# Telefon sotib olish.
# Masala. Dastur foydalanuvchida qancha pul borligin so’raydi (so’mda). 
# Foydalanuvchi olmoqchi bo’lgan texnikasining narxini USDda kiritadi. 
# Dastur texnika narxini so’mga o’girib, foydalanuvchi bu texnika ololsa, 
# “Olcha.uz dan sotib olishingiz mumkin”, agar puli yetmasa, “Mablag’ yetarli emas. 
# N so’m yetmayapti” xabarini consolega chiqaradi. Consoleda shu narsa ko’rsatilishi 
# kerak. Sonlar 0 dan keyin 2 xona yaxlitlanishi kerak.

iphone = 1300
kurs = 11250
savol = int(input("Qancha mablag'ingiz bor? : "))
narx = int((savol/kurs)-iphone)

if narx>0:
    print("Siz olcha.uz dan iphone 13 pro sotib olishingiz mumkun!")
    print(f"Iphone 13 pro narxi {iphone} $ ({iphone*kurs} so'mda).")
    print(f"Sizning ortiqcha mablag'ingiz: {narx} $ ({narx*kurs} so'mda)")
else: 
    print("Mablag' yetarli emas!")
    print(f"Sizda {int(narx*(-1))} $ ({(narx*kurs)*(-1)} so'mda) mablag' yetarli emas.")
    

