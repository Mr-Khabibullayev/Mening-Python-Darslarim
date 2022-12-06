from fuzzywuzzy import fuzz
# Bu modul yordamida so'zlarni bir-biriga solishtirish yoki matnlar tarkibida kerakli so'zni topishda foydalanamiz. 
print(fuzz.ratio("salom",'assalom'))
print(fuzz.ratio("salom","salim"))

