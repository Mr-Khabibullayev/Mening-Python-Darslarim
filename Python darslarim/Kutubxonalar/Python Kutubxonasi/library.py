import datetime as dt

# hozir = dt.datetime.now()
# print(hozir)
# print(hozir.date())
# print(hozir.time())
# print(hozir.hour)
# print(hozir.min)
# print(hozir.second)


# bugun = dt.date.today()
# print(f"Bugun sana: {bugun}")
# ertaga = dt.date(2022,12, 6)
# print(f"Ertaga sana:  {ertaga}")


# time()
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozirgi vaqt: {vaqtHozir}")
# vaqtKeyin = dt.time(19,28,23)
# print(vaqtKeyin)

# sanalar orasidagi farqni topish 
# bugun = dt.date.today()
# ramazan = dt.date(2023,3,20)
# farq = ramazan-bugun 
# print(farq)
# print(f"Ramazonga {farq.days} kun qoldi")

hozir = dt.datetime.now()
futbol = dt.datetime(2022,12,10,23,45,00)
farq = futbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} soat qoldi")




import math

# PI = math.pi
# print(f"PI ning qiymati: {PI}")
# E = math.e
# print(f"e ning qiymati: {E}")
# math.sin(math.pi/2)
# math.cos(0)
# math.tan(PI)

# print(math.degrees(math.pi/2))
# print(math.radians(90))

# math.log(5)
# math.log10(100)

# x = 4.6
# print(math.ceil(x))
# print(math.floor(x))

# yahlid = round(x)
# print(yahlid)


# x = 81 
# math.sqrt(x)

# math.pow(x,3)
# math.pow(x,5)
# math.pow(x,1/3)






# from pprint import pprint
# import json

# filename = "../bemor.json"
# with open(filename) as f:
#     bemor = json.load(f)
    
# # print(bemor)
# # pprint(bemor)

# import requests
# r = requests.get('https://api.github.com')

# pprint(r.json())


    # www.ihateragex.io




import re

# from words_list import words

# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"

# andoza = "^т...р$"

# # re.match ning vazifasi sozni mos kelishini tekshirib beradi

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))



# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza,matn)
# print(email)


# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")



