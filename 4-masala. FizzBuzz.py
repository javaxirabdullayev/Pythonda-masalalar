# 4-masala. FizzBuzz

# Foydalanuvchi son kiritadi. Kiritilgan songa qarab natija ko'rsatiladi.
# - kiritilgan son 3 ga bo'linsa -> 'Fizz' so'zi chiqadi
# - kiritilgan son 5 ga bo'linsa -> 'Buzz' so'zi chiqadi
# - kiritilgan son 3 ga va 5 ga bo'linsa -> 'FizzBuzz' so'zi chiqadi
# - kiritilgan son 3 ga ham, 5 ga ham bo'linmasa, sonning o'zi chiqadi

# Dastur.
son = float(input("Son kiriting: "))
if son % 3 == 0 and son % 5 == 0:
    print("FizzBuzz")
elif son%3==0:
    print("Fizz")
elif son%5==0:
    print("Buzz")
else:
    print(f"{int(son)} soni 3 ga ham 5 ga ham bo'linmaydi.")
    