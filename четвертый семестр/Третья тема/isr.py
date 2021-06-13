"""

Автор: Трубкина Александра Юрьевна

3.1. Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).

3.2. Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга». Создание функций для вывода на печать информации, хранящийся в объектах.

"""


# ИСР 3.1

class Written():
    def __init__(self, name ="", email ="", body ="", created="", updated = ""):
        self.__name, self.__email, self.__body, self.__created, self.__updated,  = name, email, body, created, updated
 
    @property
    def name(self):
        return self.__name

    @fname.setter
    def fname(self, new_fname):
        if (new_name != ""):
            self.__fname = new_name
        else:
            raise ValueError("Имя не может быть пустым")
            
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
    def body(self):
        return self.__body

    @sorceinfo.setter
    def sorceinfo(self, new_body):
        if (isinstance(new_body, str)) and (len(new_body) > 1):
            self.__body = new_body
        else:
            raise ValueError("Внесите информацию") 

    @property
    def created(self):
        return self.__created

    @postalcode.setter
    def created(self, new_created):
        if not isinstance(new_created, str):
            raise ValueError("Дата неверная")
        else:
            self.__created = new_created
    
    @property
    def updated(self):
        return self.__updated

    @city.setter
    def updated(self, new_updated):
        if not isinstance(new_updated, str):
            raise ValueError("Город введен некорректно")
        else:
            self.__updated = new_updated
    
    def __repr__(self):
        return 'Комментарий: {}'.format(self.__body)
