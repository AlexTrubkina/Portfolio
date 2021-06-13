class NewRegistration():
    def __init__(self, email="", fname="", sname="", password="", sorceinfo = "", address = "", postalcode = "", city = "", country = "", regtype = "", affiliation = ""):
        self.__fname, self.__email, self.__sname, self.__password, self.__sorceinfo, self.__address, self.__postalcode, self.__city, self.__country, self.__regtype, self.__affiliation = fname, email, sname, password, sorceinfo, address, postalcode, city, country, regtype, affiliation
 
    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, new_fname):
        if (new_fname != ""):
            self.__fname = new_fname
        else:
            raise ValueError("Имя не может быть пустым")

    @property
    def sname(self):
        return self.__sname

    @sname.setter
    def sname(self, new_sname):
        if (new_sname != ""):
            self.__sname = new_sname
        else:
            raise ValueError("Фамилия не может быть пустой")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str) and len(new_password) < 8:
            raise ValueError("Произошла ошибка, пароль введен некорректно")
        else:
            self.__password = new_password
            
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if not isinstance(new_email, str):
            raise ValueError("Произошла ошибка, e-mail введен некорректно")
        else:
            self.__email = new_email

    @property
    def sorceinfo(self):
        return self.__sorceinfo

    @sorceinfo.setter
    def sorceinfo(self, new_sorceinfo):
        if (isinstance(new_sorceinfo, str)) and (len(new_sorceinfo) > 100):
            self.__sorceinfo = new_sorceinfo
        else:
            raise ValueError("Информация введена некорректно") 

    @property
    def postalcode(self):
        return self.__postalcode

    @postalcode.setter
    def postalcode(self, new_postalcode):
        if not isinstance(new_postalcode, str):
            raise ValueError("Индекс введен некорректно")
        else:
            self.__postalcode = new_postalcode
    
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        if not isinstance(new_city, str):
            raise ValueError("Город введен некорректно")
        else:
            self.__city = new_city
    
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country):
        if not isinstance(new_country, str):
            raise ValueError("Государство введено некорректно")
        else:
            self.__country = new_country
   
    @property
    def affiliation(self):
        return self.__affiliation

    @affiliation.setter
    def affiliation(self, new_affiliation):
        if (isinstance(new_affiliation, str)) and (len(new_affiliation) > 150):
            self.__affiliation = new_affiliation
        else:
            raise ValueError("Аффиляция введена некорректно")
    
    @property
    def address(self):
        return self.__address
        
    @address.setter
    def adress(self, new_address):
        if (isinstance(new_address, str)) or (len(new_address) > 10):
            self.__address = new_address
        else:
            raise ValueError("Адрес должен быть длиннее 10 символов")
    
    @property
    def regtype(self):
        return self.__regtype
        
    @regtype.setter
    def regtype(self, new_regtype):
        if not (isinstance(new_regtype, str)) or (new_regtype != "IEEE members") or (new_regtype != "full registration"):
            return ValueError("Информация введена некорректно")
        else:
            self.__regtype = new_regtype

    def __repr__(self):
        str1 = 'Имя: {0}\nФамилия: {1};\nE-mail: {2};\nПароль: {3};\nАдрес: {4}; \nИндекс: {5};'
        str2 = '\nОткуда узнали о нас: {6};\nГород: {7};\nСтрана: {8};\nТип регистрации: {9};\nАффилиация автора: {10}.'
        str3 = str1 + str2
        return str3.format(self.__fname, self.__sname, self.__email, self.__password, self.__address, self.postalcode, self.__sorceinfo, self.__city,self.country, self.__regtype, self.__affiliation)

u1 = NewRegistration()
u1 = NewRegistration("example@mail.ru","Alex","Trubkina","12345678","0000000000","Улица примерная дом 35","1234567","Город","Страна","full registration", "affiliation")
print(u1)



"""

Код, который был раньше
class NewRegistration():
    def __init__(self, fname, sname, email, address, postalcode, city, sourceinfo, typeofregistration, affiliation, country):
        if (fname != "") and (sname != ""):
            self.fname = fname
            self.sname = sname
        else:
            raise ValueError("Имя и фамилия не могут быть пустыми")
        
        self.email = self.__check_email(email)
        self.sorceinfo = self.__source_check(sourceinfo)
        self.address = self.__address_check(address)
        self.postalcode = self.__postalcode_check(postalcode)
        self.city = self.__city_check(city)
        self.country = self.__country_check(country)
        self.typeofregistration = self.__typeofregistration_check(typeofregistration)
        self.affiliation = self.__affiliation_check(affiliation)

    def __postalcode_check(postalcode):
        if not isinstance(postalcode, str):
            raise ValueError("Индекс неверный")
        else:
            return postalcode
    
    def __affiliation_check(affiliation):
        if (isinstance(affiliation, str)) and (len(affiliation) > 150):
            return affiliation
        else:
            raise ValueError("Аффиляция введена некорректно")   
    
    def __city_check(city):
        if not isinstance(city, str):
            raise ValueError("Город введен неверно")
        else:
            return city
    def __country_check(country):
        if not isinstance(country, str):
            raise ValueError("Неверная информация")
        else:
            return country
            
    def __check_email(email):
        if not isinstance(email, str):
            raise ValueError("Не тот mail")
        else:
            return email

    def __address_check(address):
        if (isinstance(address, str)) or (len(address) > 10):
            return address
        else:
            raise ValueError("Адрес должен быть длиннее 10 символов")   
    def __source_check(sourceinfo):
        if (isinstance(sourceinfo, str)) and (len(sourceinfo) > 100):
            return sourceinfo
        else:
            raise ValueError("Неверная информация")   
    def __typeofregistration_check(typeofregistration):
        if not (isinstance(typeofregistration, str)) or (typeofregistration != "IEEE members") or (typeofregistration != "full registration"):
            return ValueError("Нет такого типа регистрации")
        else:
            raise typeofregistration
"""
