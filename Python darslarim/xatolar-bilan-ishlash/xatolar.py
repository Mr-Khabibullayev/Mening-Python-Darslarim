# yosh = input("Yoshigizni kiriting: ")
# yosh = int(yosh)
# print(f"siz {2202-yosh} yilda tugilgansiz . ")


# yosh = input("Yoshigizni kiriting: ")
# try:
    # yosh = int(yosh)
# except:
    # print("Iltimos butun son kiriting")
# else:
    # print(f"siz {2022-yosh} yilda tugilgansiz .")
    
    
    

# yosh = input("Yoshigizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Iltimos butun son kiriting")
# else:
#     print(f"siz {2022-yosh} yilda tugilgansiz .")
    





# x,y = 5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("sonni 0 ga bo'lib bo'lmaydi ")




# mevalar = ['olma','anor','behi','olcha']

# try:
#     print(mevalar[5])
# except IndexError:
#     print(f"Royhat {len(mevalar)} ya meva bor xolos ")


# user = {
#     'username' : 'Mr Khabibullayev',
#     'status' : 'admin',
#     'email' : 'habibulayevaxrorbek960@gmail.com'  ,
#     'phone' : '902011779'
# }
# key = 'email'
# # key = 'tel'
# try:
#     print(f"foydalanuvchi: {user[key]}")
# except:     
#     print("Bunday kalit maxjud emas.")




# fayllar bilan ishlashda xatolar

# filename = 'data.txt' #bu fayl menda mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print("Bunday hujjat mavjud emas. ")




# import json

# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']

# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         # print(f"{filename} mavjud emas")
#         pass
#     else:   
#         print(talaba['ism'])




# n = input("Butun son kiriting:  ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: 
#     print("0ga bo'lib bo'lmaydi")
# else :
#     print(f"x = {x}")



# while True:
#     yosh = input("Yoshingizni kiriting:  ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2022-yosh} yilda tugilgansiz")












