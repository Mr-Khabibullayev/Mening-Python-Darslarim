

# claslar bilan ishlash

# class Talaba :
#     def  __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
        
#     def get__name(self):
#         return self.ism
    
#     def get_last_name(self):
#         return self.familiya
#     def get_age(self,yil):
#         return yil - self.tyil
    
#     def tanishtir(self):
#         print(f"Men {self.ism} {self.familiya}, tugilgan yilim {self.tyil}")
    

# talaba1 = Talaba("olim","Hasanov",2000)
# talaba2 = Talaba("Anvar","Komilov",1994)
# talaba3 = Talaba("Axrorbek","Habibullayev",2006)


# print(talaba1.get_age(2022))









# class Talaba :
#     def  __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
        
#     def set_bosqich(self,yangi_bosqich):
#         self.bosqich = yangi_bosqich
        
#     def update_bosqich(self):
#         self.bosqich += 1
        
#     def get_name(self):
#         return self.ism  
    
#     def get_last_name(self):
#         return self.familiya
    
#     def get_bosich(self):
#         return self.bosqich
    
#     def get_age(self):
#         return self.tyil
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}.  {self.bosqich}-bosqich talabasi"

# talaba1 = Talaba("alijon","valijon",1995)

# def see_methods(klass):
#     return [method for method in dir(klass) if not method.startswith('__')]
    
# print(talaba1.get_info())


# class Fan():
#     """Fan nomli klas   """
#     def __init__(self,nomli):
#         self.nomi = nomli
#         self.talabalar_soni = 0
#         self.talabalar = []
        
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
        
#     def get_students(self):
#         return [x.get_info() for x in self.talabalar]





# matem = Fan("Oliy matematika")
# talaba1 = Talaba("alijon","valijon",1995)
# talaba2 = Talaba("Hasan","Alimov",2000)
# talaba3 = Talaba("Akrom","Boriyev",2001)
# matem.add_student(talaba1)
# matem.add_student(talaba2)
# matem.add_student(talaba3)

# print(matem.talabalar_soni)
# print(matem.talabalar)
# print(matem.talabalar[0].get_info())







# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         """Saxsning hususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
        
#     def get_info(self):
#         """Shaxs haqida ma'lumotlarni beradi"""
#         info = f"{self.ism} {self.familiya}." 
#         info += f"Passport:{self.passport}. {self.tyil}- yilda tug'ilgan"
#         return info
    
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil


# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism,familiya,passport,tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
        
#     def get_id(self):
#         """Talabaning ID raqami """
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}." 
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam }"
#         return info
    

# class Manzil :
#     """Manzilni saqlash uchun klass"""
#     def __init__(self,uy,kocha,tuman,viloyat):
#         """Manzil hususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
        
#     def get_manzil(self):
#         """Manzilni korish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil
    
    
    
# talaba1_manzil = Manzil(2,"sarkor","baliqchi", "andijon")
# talaba1 = Talaba("Olim","Kamolov","F00n2314",2010,"N00002",talaba1_manzil)    
    
    















# from uuid import uuid4
# class Avto :
#     """Avtomobil klassi"""
#     __num_avto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobil xususiyatlarii"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
#
#
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
#
#     def get_km(self):
#         return self.__km
#
#     def get_id(self):
#         return self.__id
#
#     def add_km(self,km):
#         """Mashinaning km ga yana km qo'shadigan metod"""
#         if km >= 0 :
#             self.__km += km
#         else:
#             print("Mashinaning km kamaytirib bo'lmaydi")
#
#
#
# class Buss:
#     pass
#
# class Train:
#     pass
#


from uuid import uuid4


class Avto:
    """Avtomobil klassi"""
    __num_avto = 0

    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomobil xususiyatlarii"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    # def __str__(self):
    #     """Vazifasi obyek haqida string holatda malumotlar olishimiz  mumkin"""
    #     return f"Avto: {self.make} {self.model}"
    
    def __repr__(self):
        """Vazifasi obyek haqida string holatda malumotlar olishimiz  mumkin"""
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self,y):
        return self.narh == y.narh
    
    def __lt__(self,y):
        return self.narh < y.narh
    
    def __le__(self,y):
        return self.narh <= y.narh

    def __len__(self):
        return self
    
    




class Avtosalon:
    """Avtosalon klassi"""
    
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            
            else:
                print("Avto kiritng")
    
    def __len__(self):
        return self.avtolar[0]
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index] = qiymat
    
    

salon1 = Avtosalon("MaxAvto")
avto1 = Avto("GM","Malibu","qora",2020,1000)
avto2 = Avto("GM","Lasetti","Oq",2020,2000)
avto3 = Avto("Toyota","Carolla","sariq",2010,3000)
salon1.add_avto(avto1,avto2,avto3)
print()

# isnistance() funksiyasi orqali biz qiymat qaysi oraliqga yoki qaysi ozgaruvchi turiga kirishini aniqlab olishimiz mumkin
isinstance(4,int)







