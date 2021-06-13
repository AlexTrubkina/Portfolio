

import sqlite3


conn = sqlite3.connect('example.db')

#дз удалить все данные рхед, и что-то еще сделать с фильтрами - два завроса - на удаление на обновление(хотя бы знать)

c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE stocks
             #(date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data

def f_insert():
    values = [('2020-02-20', 'BUY', 'APL', 100, 42.00)]
    try:
        c.executemany(f'INSERT INTO stocks VALUES (?, ?, ?, ?, ?)', values)
        conn.commit()
    except sqlite3.Error as error:
        print("Не получилось обновить таблицу ", error)

def f_update():
    price = 10.4
    symbol = "APL"
    try:
        c.execute('UPDATE stocks SET price = ? WHERE symbol = ?', (price, symbol))
        conn.commit()
    except sqlite3.Error as error:
        print("Не получилось обновить таблицу", error)
    

def f_delete():
    try:
        c.execute("DELETE FROM stocks WHERE price = 56.0")
        conn.commit()
    except sqlite3.Error as error:
        print("Не получилось обновить таблицу ", error)


def main():
    print("Хотите просто увидеть содержимое таблицы?(y/n)")
    answ = input()
    if(answ == 'n'):
        f_insert()
        f_update()
        f_delete()
    if(answ == 'y'):
        for row in c.execute('SELECT * FROM stocks ORDER BY price'):
            print(row)
    if(answ != 'y' and answ != 'n'):
        print('Вы ввели неверные данные.')
    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
            print(row)
    



main()

# Save (commit) the changes


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
