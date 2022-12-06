"""Fayllar bilan ishlash"""

# file = open("pi.txt")
# print(type(file))
# PI = file.read()
# print(PI)
# file.close()

## width operatori file ni ozi yopadi:
# with open('pi.txt') as file:
#     pi = file.read()
    
# print(pi)


# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = float(pi) 
# print(pi)




# filename = 'data/talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)
        
        
# with open(filename) as file:
#     taalabalar = file.readlines()
    
# taalabalar = [talaba.rstrip() for talaba in taalabalar]
# print(taalabalar)




###   yangi faylga malumotlarni yozish:::


# faylnomi = 'new_fayl.txt'
# ism = 'Olimov Hasanboy'
# tyil = 2004
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism + '\n')
#     fayl.write(str(tyil) + '\n')




###   elementlarni qoshish


# faylnomi = 'new_fayl.txt'
# with open(faylnomi, 'a') as fayl:
#     fayl.write("Alijon Valiyav \n")
#     fayl.write("2000")





### lugatlarni royhatlarni saqalsh

import pickle

talaba1 = {'ism': 'husan','familiyasi':'husanov','tyil':2003,'kurs':2}
talaba2 = {'ism': 'alijon','familiyasi':'valiyev','tyil':2004,'kurs':1}



with open('info.pkl','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)









