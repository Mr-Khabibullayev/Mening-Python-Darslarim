#####      eng muhim translater vazifasini otaydi


from googletrans import Translator
tarjimon = Translator()
# matn_uz = "Python - dunyodagi eng mashhur dasturlash tili"

# tarjima = tarjimon.translate(matn_uz)
# print(tarjima.origin)  #  bu asl matni saqlaydi
# print(tarjima.text)  # bu esa tarjima qilingan matnni saqlaydi
# print(tarjima.src) # bu esa matnni qaysi tilda ekanlgini aniqlab beradi

# ##### dest='' metodi orqali bi ozimiz istagan tilni tanlab olishimiz mumkin
# tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
# print(tarjima_ru.text)

matn_en = "Tashkent is the capital of Uzbekitan"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')
print(tarjima_uz.text)




# tarjimon = Translator()

# msg = "Tarjima uchun so'z kiriting (chiqib ketishish uchun \"q\ deb yozing): "
# while True :
#     text = input(msg)
#     if text =="q":
#         break
#     else :
#         tarjima = tarjimon.translate(text, src='uz' ,dest='en')
#         print(tarjima.text)