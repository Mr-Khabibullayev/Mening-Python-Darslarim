######      String metodlar      ######

# ism = "salom"
# fmiliya = "habibullayev"
# ism_sharf = f"{ism} {fmiliya}"
# print(ism_sharf.upper())
# print(ism_sharf.lower())
# print(ism_sharf.title())
# print(ism_sharf.capitalize())


# Bo'shliqlarni olib tashlash  uchun

# meva = "    olma    "
# print(" Men " + meva.lstrip() + " yaxshi koraman")
# print(" Men " + meva.rstrip() + " yaxshi koraman")
# print(" Men " + meva.strip() + " yaxshi koraman")
# print(" Men " + meva + " yaxshi koraman")

 
# Inputlar

# ism = input("Ismingiz Nima ?")
# # print("Assalomu alaykum, " + ism )

# ism = input("Ismingiz Nima ?\n>>>")
# print("Assalomu alaykum, " + ism.title() )


# a = 80
# b = 8.8
# temp = 36.6
# print(type(b))



# ahli_soni = 7_567_876_234
# print("bugunga kelib aholi soni " ,ahli_soni)



# yosh = 36
# ism = 'Jobir'
# xabar = ism + " " +  str(yosh) + ' yoshda'
# print(xabar)


# t_yilli = int(input("Tug'ilgan yilingizni kiriting !!!"))
# yosh = 2022 - t_yilli
# print("Siz ", yosh , "yoshda ekansiz")
 
 





#######      MASSIV METODLARI       ####### 
 

 
# append() vazifasi oxriga qo'shadi
 
# mevalar = ['olma','orik','shaftoli','nok']
# print(mevalar)
# mevalar.append('banan')
# print(mevalar)




# insert() vazifasi belgilangan joydan qo'shadi


# mevalar = ['olma','orik','shaftoli','nok']
# print(mevalar)
# mevalar.insert( 3,'banan')
# print(mevalar)

# del   vazifasi indexsidagi elementni ochiradi.


# cars = ['lasetti','damas','matiz','kobalt','tiko','assalomu aleykum']
# print(cars)
# del cars[5]
# print(cars)



# remove()  vazifasi metodni nomi yoziladi va zoyilgan , metodni qidirib topib ochiradi 

# cars = ['lasetti','damas','matiz','kobalt','tiko','assalomu aleykum']
# print(cars)
# cars.remove('lasetti')
# print(cars)


# pop() vazifasi elementni massiv ichidan sug'urib oladi
# agar pop() metodidan foydallanganimizda uning ichiga qiymat kiritmasak u doim royhat ohiridan sugutib oladi

# bozorlik = ['yog','banan','guruch','tut','olma','anor']
# mahsulot = bozorlik.pop(3)
# print('Men ' + mahsulot + ' sotib oldim')
# print('Olinmagan mahsulotlar: ' , bozorlik)



# sort() metodi vazifasi elementlarni alifbo boyicha saralaydi va sonlarni ham

# cars = ['Bmw','audi','mers','toyota','hyundai','kia','chevrolet','ravon','bugati','ferrari']
# cars = ['bmw','audi','mers','toyota','hyundai','kia','chevrolet','ravon','bugati','ferrari']
# cars.sort()
# print(cars)
# numbers = [34,-3,9,23,12,11,1,100,-100]
# numbers.sort()
# print(numbers)


# sort(reverse=True) metodni vazifasi elementni teskari tartibda saralaydi va sonlarni ham
# cars = ['bmw','audi','mers','toyota','hyundai','kia','chevrolet','ravon','bugati','ferrari']
# cars.sort(reverse=True)
# print(cars)
# numbers = [34,-3,9,23,12,11,1,100,-100]
# numbers.sort(reverse=True)
# print(numbers)


# sorted() metodini vazifasi massivni oziga tegmasdan uni togri tartibda tartiblash va sonlarni ham
# cars = ['bmw','audi','mers','toyota','hyundai','kia','chevrolet','ravon','bugati','ferrari']
# print(cars)
# print(sorted(cars))
# numbers = [34,-3,9,23,12,11,1,100,-100]
# print(sorted(numbers))


# sorted(cars, reverse=True) metodini vazifasi massivni oziga tegmasdan uni teskari tartibda  tartiblash va sonlarni ham
# cars = ['bmw','audi','mers','toyota','hyundai','kia','chevrolet','ravon','bugati','ferrari']
# print(cars)
# print(sorted(cars,reverse=True))
# numbers = [34,-3,9,23,12,11,1,100,-100]
# print(sorted(numbers,reverse=True))



# reverse() vazifasi royhatni teskarisiga aylantirib qiyadi
# cars = ['bmw','audi','mers','toyota','hyundai','kia','chevrolet','ravon','bugati','ferrari']
# print(cars)
# cars.reverse()
# print(cars)


# len() vazifasi massivni uzunligini aniqlaydi
# cars = ['bmw','audi','mers','toyota','hyundai','kia','chevrolet','ravon','bugati','ferrari']
# uzunlik = len(cars)
# print(uzunlik)


# range() vazifasi va list() ning vazifasi 
# range(0,10) sonlar oraligini olib beardi va ikkinchi index gacha bolgan sonlarni qabul qiladi 
# ragne(birinchi index , ikkinchi index , qadamlar soni)
# list() vazifasi esa range() metodidan kelgan sonlardan massiv yaratib beradi

# sonlar = list(range(0,10))
# print(sonlar)

# toq_sonlar = list(range(1,20,2))
# print(toq_sonlar)
# juft_sonlar = list(range(0,20,2))
# print(juft_sonlar)
# sanash = list(range(0,101,10))
# print(sanash)



# max(ozgaruvchi nomi) vazifasi massivni ichidagi sonlarni maxsimal qiymatimni aniqlab beradi
# min(ozgaruvchi nomi) vazifasi massivni ichidagi sonlarni minimal qiymatimni aniqlab beradi
# sum(ozgaruvchi nomi) vazifasi massivni ichidagi sonlarni yigindisini chiqarib beradi

# sonlar = list(range(0,20))
# minimum = min(sonlar)
# print(minimum)
# maxsimum = max(sonlar)
# print(maxsimum)
# yigindi = sum(sonlar)
# print(yigindi)


# massivni ichidan kesish usullari
# cars = ['bmw','audi','mers','toyota','hyundai','kia','chevrolet','ravon','bugati','ferrari']
# print(cars[:5])
# print(cars[0:])
# print(cars[2:5])


# massivdan nusha olish

# cars = ['bmw','audi','mers','toyota','hyundai','kia','chevrolet','ravon','bugati','ferrari']
# myCars = cars[:] # buning vazifasi nusxa oladi va ozgarish bittasiga tasir qiladi
# myCars = cars  # buning vazifasi esa massivni tenglab qoyadi va ozgarish ikkisiga ham tasir qiladi
# myCars.remove('bmw')
# myCars[0] = 'lassettt'
# print(myCars)
# print(cars)



#####    TYPLE    #####
###   O'ZGARMAS ROYHAT TURI
# bu turdagi royhat ustida kop metodlar ishalamaydi

# toys = ('bear','car','dino','snake','lizard','bus')
# print(toys)
# toys = list(toys)
# toys.append('bmw')
# toys = tuple(toys)
# print(toys)





########     for tsikli bilan ishalsh     #######

# mehmonlar = ['Ali','Vali','Hasan','Husan','Olim','Anvar','Azamat']

# for mehmon in mehmonlar:
#     print('salom', mehmon)
#     print('hayr', mehmon)

# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon} , sizni 20 dekabr kuni nahorga oshga taklif etamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")


# sonlar ustida 

# sonlar = list(range(11))
# for son in sonlar:
#     print(f"{son} ning kavadrati {son ** 2} ga teng")

# sonlar = list(range(11))
# sonlar__kvadrati = []
# for son in sonlar:
#     sonlar__kvadrati.append(son**2)


# dostlar = []
# print('5 ta eng yaqin do\'stingiz')
# for n in range(5):
#     dostlar.append(input(f"{n+1} - dostingizning ismini kitriting: "))
# print(dostlar)




#######     Tarmoqlanish     ######
### if a elselar   ###

# avtolar = ['audi','bmw','volvo','kia','hyudai']

# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())


# ism = input('Ismingiz nima?\n>>>')
# if ism.lower() != 'ali' :
#     print(f'Uzr {ism.title()} biz Alini kutayapmiz')

# else:
#     print('Salom, Ali')




# javob = float(input('12x6 nechiga teng?>>>'))
# if javob == 72:
#     print('Javob togri')
# else:
#     print('Javob hato')




# yosh = int(input('Yoshingiz nechida? >>>'))
# if yosh >= 18:
#     print('Xush Kelibsiz!')
# else:
#     print('Kirish mumkin emas!')


# login = input('Yangi login tanlang:')
# if len(login) <= 5:
#     print('Login 5 harfdan ko\'proq bolishi shart!')
# else:
#     print('Login almashtirildi')


# yil = int(input("Tug\'ilgan yilingizni kiriting:"))
# if 2020-yil < 18 :
#     print(f"Yshingiz {2020-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print('Xush kelibsiz!')


# yosh = int(input("Yoshingiz nechida?"))
# if yosh>65 : print("Siz COVID-19 risk guruhida ekansiz ")


# x,y = 25,50
# print('x>y') if x>y else print('x<y')


# yosh = int(input("Yoshingiz nechida? "))
# if yosh <= 4:
#     narh = 0
# elif yosh <= 12:
#     narh = 5000
# elif yosh <= 18:
#     narh = 8000
# else:
#     narh = 10000
# print(f'Sizga kirish {narh} so\'m')



####    and va or operatorlari ishlatilishi



# kun = input('Bugun qaysi kun ? >>> ')
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni ')
# else:
#     print('Bugun ish kuni.')


# kun = input('Bugun qaysi kun ?')
# harorat = float(input("Havo harorati qanday? "))

# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print("Cho'milgani ketdik!")
# elif kun.lower() == 'yakshanba' and harorat <= 30:
#     print("Uyda dam olamiz")
# else:
#     print('Bugun ish dam olish yoq')



####   in va not in  oparetorlari
## in  vazifasi elementni massivni ichida borligini tekshiradi
## not in vazifasi elementni massivda ichida yoqligini tekshiradi



# menu = ['manti','somsa','shashlik','assorti']
# bolen = 'manti' in menu
# print(bolen)


# menu = ['manti','somsa','shashlik','assorti','osh','norin','qozonkabob']
# ovqat = input("Nima ovqat yeysiz? >>> ")
# if ovqat.lower() not in menu:
#     print('Afsus bizda bu turdagi ovqat mavjud emas')
# else:
#     print('Buyurtma qabul qilindi.')



# menu = ['somsa','shashlik','assorti','osh','norin','qozonkabob']
# buyurtmalar = ['osh','somsa','manti','shashlik']
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f'Menuda {taom} bor')
#         else:
#             print(f"Kechirasiz, menuda {taom} yo\'q")
# else:
#     print('Savatchangiz bo\'sh')





#######      Yangi ma'lumot turi <<< Lug'at >>> bilan tanishamiz   yani obyekt bilan     #######


# car_0 = {'model': 'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])


# en_uz = {
#     'apple':'olma',
#     'apricot':'o\'rik',
#     'banana':'banan'
# }
# print(en_uz)
# print(en_uz['banana'])


# mevalaar = {'olma':10000,'tarvuz':8000,'qovun':10000}
# print(f'Olma narhi {mevalaar["olma"]} som\'')


# talaba = {'ism':'murod olimov','yosh':20,'t_yili':2000}
# print(f"{talaba['ism'].title()} , \nfrom django.utils.translation import \n{talaba['t_yili']}-yilda tug'ilgan, \n{talaba['yosh']} yoshda ")




 

# yangi lugat kiritish yani yana bitta obyekt qoshish yoki ozgartirish mumkin yana bo'sh lugat ham yaratish mumkin



# bosh = {}
# talaba = {'ism':'murod olimov','yosh':20,'t_yili':2000}
# print(talaba)
# talaba['kurs'] = 4
# talaba['fakultet'] = 'informatika'
# talaba['ism'] = 'abdulloh'
# print(talaba)

# bosh = {}
# bosh['kurs'] = 4
# bosh['fakultet'] = 'informatika'
# bosh['ism'] = 'abdulloh'
# print(bosh)
# print(f"Talaba {bosh['ism'].title()} {bosh['kurs']} - kurs")


#####    lugatning ichidagi malunotni ochirish

# talaba = {'ism':'murod olimov','yosh':20,'t_yili':2000}
# del talaba['ism']
# print(talaba)


#####   get() metodi ichidan tekshiradi

# talaba = {'ism':'murod olimov','yosh':20,'t_yili':2000}
# phone = talaba.get('ism','Bunday ism mavjud emas')
# # phone = talaba.get('ali','Bunday ism mavjud emas')
# print(phone)


# talaba = {'ism':'murod olimov','yosh':20,'t_yili':2000}
# phone = talaba.get('ali')
# print(phone)



#####      Lug'atlar bilan ishlash


# talaba = {
#     'ism': 'alijon',
#     'familiyasi':'shamsiyev',
#     'yosh': 22,
#     'fakultet':'matematika',
#     'kurs': 4
# }

# print(talaba.items())

# for kalit , qiymat in talaba.items():
#     print(f'Kalit: {kalit}')
#     print(f'Qiymat: {qiymat} \n')



# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310'
# }

# for k, q in telefonlar.items():
#     print(f'{k.title()}ning telefoni {q}')


# mahsulotlar = {
#     'olma': 10000,
#     'anor': 20000,
#     'uzum': 40000,
#     'anjir':25000,
#     'shaftoli':30000
# }
# print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlari:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# print('Do\'kondagi mahsulotlari:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
    
# print('Do\'kondagi mahsulotlari:')
# for mahsulot,narhlari in mahsulotlar.items():
#     print(f'{mahsulot.title()}ning narhi {narhlari} so\'m') 



# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f'{mahsulot.title()} {mahsulotlar[mahsulot]} so\'m')
#     else :
#         print(f'{mahsulot.title()} afsuski yoq ekan')

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f'Iltimos, do\'koningizga {buyum} ham olib keling')






#######   Lug'at elementlarini tartib bilan chiqarish


# mahsulotlar = {
#     'olma': 10000,
#     'anor': 20000,
#     'uzum': 40000,
#     'anjir':25000,
#     'shaftoli':30000
# }
# print("Do'koningizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())






####  obyektni valuelarini chiqarish uchun value() dan foydalanamiz

# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310'
# }

# print(telefonlar.values())


# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)








# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir': 'iphone x',
#     'umar':'iphone x'
# }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)
    

#####     elementlarni takrorlamasdan chiqarish uchun set() funksiyasidan foydalanamiz va malumot turi hisoblanadi


# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)




#### hech qachon bitta elementni yana chiqarmaydi

# toys = {'ball','car','lamp','ball'}
# print(toys)









#####    Lug'atlar royhati


# car0 = {
#     'model':'lacetti',
#     'rang':'oq',
#     'yil': 2018,
#     'narh':13000,
#     'km':50000,
#     'korobka':'avtomat'
# }
# car1 = {
#     'model':'nexia 3',
#     'rang':'qora',
#     'yil': 2015,
#     'narh':9000,
#     'km':89000,
#     'korobka':'mexanika'
# }
# car2 = {
#     'model':'gentra',
#     'rang':'qizil',
#     'yil': 2019,
#     'narh':15000,
#     'km':20000,
#     'korobka':'mexanika'
# }


# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang , "
#       f"{car['yil']} - yil , {car['narh']}$")



# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang , "
#       f"{car['yil']} - yil , {car['narh']}$")



# car = car2
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang , "
#       f"{car['yil']} - yil , {car['narh']}$")



# cars = [car0,car1,car2]
# print(type(cars))

# for car in cars :
#     print(f"{car['model'].title()}, "
#       f"{car['rang']} rang , "
#       f"{car['yil']} - yil , {car['narh']}$")



# car0 = {
#     'model':'lacetti',
#     'rang':'oq',
#     'yil': 2018,
#     'narh':13000,
#     'km':50000,
#     'korobka':'avtomat'
# }
# car1 = {
#     'model':'nexia 3',
#     'rang':'qora',
#     'yil': 2015,
#     'narh':9000,
#     'km':89000,
#     'korobka':'mexanika'
# }
# car2 = {
#     'model':'gentra',
#     'rang':'qizil',
#     'yil': 2019,
#     'narh':15000,
#     'km':20000,
#     'korobka':'mexanika'
# }
# cars = [car0,car1,car2]
# print(cars[0]['narh'])










#######     While Do funksiyasi

# ism = input("Ismingiz nima ?")
# savol = f'Salom {ism.title()}. Yoshingiz nechida?'
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha mert ?")
# height = float(height)
# print(height)



#####    while()  funksiyasi

# son = -10
# while son <= 5:
#     print(son, end=' ')
#     # son = son +1
#     son += 1
# print('dastur tugadi')

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son Kiriting"
# savol += "(dasturni toxtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
#     else:
#         print('funksiya yakunlandi')




# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son Kiriting"
# savol += "(dasturni toxtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#         print('funksiya yakunlandi')
#     else:
#         print(float(qiymat)**2)




# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son Kiriting"
# savol += "(dasturni toxtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         print('funksiya yakunlandi')
#         break
#     else:
#         print(float(qiymat)**2)
        
        
# son = 0
# chegara = 10
# while True:
#     son += 1
#     if son == chegara:
#         print('funksiya yakunlandi')
#         break
#     else:
#         print(son)


#####  break toxtatadi
#####  continue ning vazifasi kodni tashlab otib ketadi


# sonlar = list(range(1,11))
# for son in sonlar :
#     if son == 5:
#         continue
#         # break
#     print(f'{son} ning kvadrati {son**2} ga teng')



# son = 0
# while son < 10:
#     son += 1
#     if son % 2 !=1:
#         continue
#     else:
#         print(son)




##   1. foydalanuvchidan  yaxshi korgan kitoblarini sorang. Foydalanuvchi stop sozini kiritishi bilan dasturni totating


# savol = "Yoqtirgan kitobingiz kiriting:  "
# ishora = True
# kitoblar = []

# while ishora:
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         kitoblar.append(str(qiymat))
#     else:
#         print(kitoblar)
#         break


###   1. Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).


# yosh = 'Marhamat yoshingizni kiriting:  '
# ishora = True 

# while ishora:
#     qiymat = int(input(yosh))
#     if qiymat <= 7:
#         print('Sizning chiptangiz 2000 so\'m')
#     elif qiymat <= 18:
#         print('Sizning chiptangiz 3000 so\'m')
#     elif qiymat <= 65:
#         print('Siznign chiptangiz 10000 so\'m')
#     else:
#         print('Sizga chipta bepul')






####   while tsiklda royhatlar   



# print('Yaqin dostlaringiz royhatini tuzamiz')
# ismlar = []
# n = 1
# while True:
#     savol = f'{1}-dostingizni ismini kiriting: '
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input('Yana ism qoshasimi? (ha/yoq)')
#     n += 1
#     if takrorlash != 'ha':
#         break

# print('Do\'stlaringiz royhati:')
# for ism in ismlar:
#     print(ism.title())





# print('Dostlaringiz yoshini saqlaymiz.')
# dostlar = {}
# ishora = True

# while ishora:
#     ism = input("Do'stlaringiz ismini kiriting: ")
#     yosh = input(f'{ism.title()}ning yoshini kiriting: ')
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana ma'lumot qoshasizmi? (ha/yoq)")
#     if javob == 'yoq':
#         ishora = False
        
        
# for ism ,yosh in dostlar.items():
#     print(f'{ism.title()} {yosh} yoshda')









# cars = ['nexia','lasetti','matiz','nexia','toyota','audi','malibu','nexia']
# car = 'lasetti'
# while car  in cars:
#     cars.remove(car)
# print(cars)




# talabalar = ['hasan','husan','olim','botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f'{talaba.title()}ning bahosini kiriting: ')
#     print(f'{talaba.title()} baholanadi')
#     baholangan_talabalar[talaba] = int(baho)
    

# for talabaa, bahosi in baholangan_talabalar.items():
#     print(f'{talabaa.title()}ning bahosi {bahosi} ')






# # #   Masalalar


## 1 Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang va mahsulotlarni narhini ham qoshing.

## Javob:


# savol = 'Sotib oladigan mahsulotlaringizni nomini yozing (toxtatish uchun \' stop \' deb yozing): '
# mahsulot_nomi = []
# ishora = True
# while ishora:
#     qiymat = input(str(savol))
#     if qiymat == 'stop':
#         ishora = False
#     elif qiymat == '':
#         continue
#     else:
#         mahsulot_nomi.append(qiymat)


# ogirligi = "necha kilo olasiz ?"
# royhat = {}
# while mahsulot_nomi:
#     mahsulotlar = mahsulot_nomi.pop()
#     qiymat = input(f"{mahsulotlar}dan {ogirligi}")
#     royhat[mahsulotlar] = int(qiymat)
    
# f = 1
# for mahsulot , index in royhat.items():
#     print(f"{f}. {mahsulot}dan {index} kg")
#     f = f + 1
    
    
    





######      FUNCTIONS (funksiyalar)


# def salom_ber():
#   print("Assalomu aleykum")
    
# salom_ber()

# def salom_ber(ism):
#     print(f"Assalomu aluykum, hurmatli {ism.title()} !")

# salom_ber('hasan')
# salom_ber('olim')


# def salom_ber(ism , familiya):
#     """Foydalanuvchining ism familiyasini chiqaruvchi funksiya  """
#     print(f"Foydalanuvchi ismi : {ism.title()} \n"
#           f"Foydalanuvchi familiyasi : {familiya.title()}")

# salom_ber('hasan','hakimov')
# salom_ber('olim','hasanov')
# print(salom_ber.__doc__)


# def yosh_hisobla(ism,tugilgan_yil) :
#     """Foydalanuvchinig yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2022-tugilgan_yil} yoshda")
    
# yosh_hisobla('olim',1997)
# yosh_hisobla(1997,'olim')
# yosh_hisobla(tugilgan_yil=1997,ism='olim')



# def yosh_hisobla(tugigan_yil,joriy_yil=2020):
#     """Foydalanuvchining tugilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tugigan_yil} yoshdasiz" )
    
# yosh_hisobla(1995,2020)
# yosh_hisobla(1993)





######      Funksiyalarda qiymat qaytarish




# def toliq_ism_yasa(ism,familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
    
# talaba = toliq_ism_yasa('olim','olimov')
# print(talaba)
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')

# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")




# def toliq_ism_yasa(ism,familiya,otasini_ismi = ''):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasini_ismi:
#         toliq_ism = f"{ism} {otasini_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()


# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov' ,'abrorovich')

# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")





# def avto_info(kopmpaniya,model,rangi,korobka,yili,narhi=None):
#     avto = {
#         'kompaniya':  kopmpaniya,
#         'model': model,
#         'rang': rangi,
#         'korobka': korobka,
#         'yil': yili,
#         'narh' : narhi
#     }
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1,avto2]
# print('Onlayn bozordagi mavjud avtomashinalar: ')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narh: {narh}")
# # print(avtolar)



# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar

# print(oraliq(0,10))
# print(oraliq(10,21))



####    qadamlar bilan 

# def oraliq(min,max,qadam):
#     sonlar = []
#     while min<max:
#         min+=1
#         if min % qadam == 0:
#             sonlar.append(min)
#     return sonlar

# print(oraliq(0,10,3))
# print(oraliq(10,21,3))








# def avto_info(kopmpaniya,model,rangi,korobka,yili,narhi=None):
#     avto = {
#         'kompaniya':  kopmpaniya,
#         'model': model,
#         'rang': rangi,
#         'korobka': korobka,
#         'yil': yili,
#         'narh' : narhi
#     }
#     return avto


# print("Saytimizda avtolar royhatini shaknlantiramiz.")
# avtolar = []
# while True:
#     print("\n Quyidagi ma'lumotlarni kiriting ")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#     avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi))
#     javob = input("Yana avto qoshasizmi ? (yes/no): ")
#     if javob == 'no':
#         break
# print("\n Salonimizdagi avtolar")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "No'malum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi {narh}")





######      Funksiyaga Royhat Uzatish 



# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}  ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar


# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar[:])
# print(baholar)





# def katta_harf(ism):
#     katta_ism = []
#     while ism :
#         katta__harfga = ism.pop()
#         katta_ism.append(katta__harfga.title())
    
#     return katta_ism

# ismlar = ['ali','vali','hasan','husan']
# kattalar = katta_harf(ismlar[:])
# print(kattalar)


# def katta_harf(ism):
#     katta_ism = []
#     while ism :
#         katta_ism.append(ism.pop())
    
#     return katta_ism

# ismlar = ['ali','vali','hasan','husan']
# kattalar = katta_harf(ismlar[:])
# print(kattalar)
# print(ismlar)





####     *arguments


# def summa(*sonlar):
#     """Kiritilgan sonlarni yigindisni hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar :
#         yigindi += son
#     return yigindi


# print(summa(1,2))
# print(summa(1,2,5,6))


# def summa(*sonlar):
#     """Kiritilgan sonlarni yigindisni hisoblaydigan funksiya"""
#     return sum(sonlar)

# print(summa(1,2))
# print(summa(1,2,5,6))


# def summa(x,y,*sonlar):
#     """Kiritilgan sonlarni yigindisni hisoblaydigan funksiya"""
#     return   x + y + sum(sonlar)

# print(summa(1,2,4,4,3,2))
# print(summa(1,2,5,6))





#####   **keywordarguments

# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqida malumotlarni lugat korinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar

# avto1 = avto_info("GM",'malibu',rang = 'qora',yil = 2018)

# print(avto1)









# import math

# x = 400

# #  sonni ildizini topish
# print(math.sqrt(x))

# # sonni darajasini topish
# print(math.pow(5,3))

# #  Matematik pi ning qiymatini topish
# print(math.pi)

# #  2 ni darajasini topish
# print(math.log2(8))
# print(math.log2(9))


# #  10ni darajasini topish
# print(math.log10(10000))


# import random as r

# son = r.randint(0,100)
# print(son)


# import random as r

# ismlar = ['olim','anvar','husan','hasan']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))

# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))




##  massivni aralashtirib yuboradi
# import random as r

# x = list(range(0,10))
# r.shuffle(x)
# print(x)









####   Funksiyalar songi soz 





###    lambda funksiyasi

# lambda argument1,a2,a3 :ifoda 

# import math

# uzunlik = lambda pi, r: 2*pi*r

# print(uzunlik(math.pi,10))


# kvadrat = lambda x,y : x**y
# print(kvadrat(3,2))


# def daraja(n):
#     return lambda x: x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)}ga ,"
#       f"kubi esa {kub(3)}ga teng")




##   sqrt ning vazifasi sonlarni ildizini topishga yozdam beradi

# from math import sqrt


# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)



# sonlar = list(range(11))

# def daraja(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(list(map(daraja,sonlar)))



# sonlar = list(range(11))
# kvadratlar = list(map(lambda x: x*x,sonlar))
# print(kvadratlar)

# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
    
# print(kvadratlar)



# a = [4,5,6,]
# b = [7,8,9,]
# a_plus_b = list(map(lambda x,y: x+y,a,b))
# print(a_plus_b)



# import random as r

# ## random qilib beradi
# sonlar = r.sample(range(100),10)
# print(sonlar)
# def juftmi(x):
#     """x juft bolsa True Aks holda False qaytaradi"""
#     return x % 2 == 0  

# # juft_sonlar = list(filter(juftmi,sonlar))
# # print(juft_sonlar)

# juft_sonlar = list(filter(lambda son : son % 2 == 0,sonlar))
# print(juft_sonlar)



# ####    startswith()  metodi sozni bosh harifini tekshiradi boolen qaytaradi
# mevalar = ['olma','anor','anjir','shaftoli','o\'rik','tarvuz','qovun','banan']
# harf = ''
# mevalar_b = list(filter(lambda meva : meva.startswith(harf),mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva : len(meva)<=5,mevalar))
# print(mevalar2)

