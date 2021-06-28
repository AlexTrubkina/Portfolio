"""
Автор: Трубкина А.Ю.

Разработать программу, позволяющую генерировать уникальные
идентификаторы: UUID (universally unique identifier). Структура UUID — на усмотрение студента.

"""
import uuid

import random
def uniqueid():
    id_num = random.getrandbits(32)
    while True:
       yield id_num
       id_num += 1


uniqueID= uniqueid()
id1 = next(uniqueID)
id2 = next(uniqueID)

print(id1)
