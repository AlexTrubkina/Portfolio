import sqlite3
import functools
import json

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            inner.called = True
        return func(*args, **kwargs) 
    inner.called = False 
    return inner

@once
def connect_to_db(path_to_db):
    connection = None
    if (path_to_db):
        try:
            connection = sqlite3.connect(
                'file:' + path_to_db + '?mode=rw', uri=True)
            # connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}

    return connection
    

conn_dict = connect_to_db('example.db')
conn, cur = conn_dict["conn"], conn_dict["cursor"]

def wrapper(func):
    @functools.wraps(func)
    def security():
        try:
            with open('users.json', 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f) 
                    print(data)
                    members = data["members"]
                    print("Пользователи: ", members)
                    for i in range(len(members)):
                        user = members[i]
                        print("Данные о пользователе: ", user)
                        name = user["login"]              
                        pswrd = user["pass"] 
                        role = user["role"]             
                        checking(name, pswrd, role)
                except json.decoder.JSONDecodeError as e:
                    print("Что-то пошло не так: ", e)
        except FileNotFoundError as e:
            print("Такого файла не существует: ", e)
    return security

def checking(name, pswrd, role):
    try:
        check = cur.execute("SELECT* FROM users WHERE login=? and pass=?", (name, pswrd))
        res = check.fetchone()
        if(res != None):
            if(role == 0):     
                print("root")                 
                return 0
            elif(role == 1):
                print("admin") 
                return 1
            else: 
                print("user") 
                return 2
        else:
            print("Не зарегистрирован")  
            return None 
    except sqlite3.Error as e:
        print(e)

    
@wrapper
def private_zone_area():
    return "private_zone_area"


def get_users_from_table(conn, table):
    sql_query = "SELECT * FROM " + str(table)
    cursor = conn.cursor()
    res = cursor.execute(sql_query)
    users_lst = res.fetchall()
    print(users_lst)
    return users_lst

conn_dict = connect_to_db('example.db')
conn, cur = conn_dict["conn"], conn_dict["cursor"]

# 2 вариант
try:
    sql_query = '''CREATE TABLE users
             (login text, pass text, role int)'''
    cur.execute(sql_query)
except sqlite3.OperationalError as e:
    e_str = str(e)

    if ("already exists" in e_str):
        print(f' NOTICE: {e}. CONTINUE ')
       
        #sql_query = '''INSERT INTO users VALUES (?, ?, ?)'''
        #users_lst = [('root', '123', 0), ('admin', '789', 1), ('user', 'qwe', 2)]
        #try:
            #cur.executemany(sql_query, users_lst)
            #conn.commit()
        #except sqlite3.Error as e:
            #print(f'Error with adding users to db. {e}')


get_users_from_table(conn, 'users')  
private_zone_area()
       
#wrapper(get_users_from_table(conn, 'users'))
#print(users)

conn.close()
cur, conn = None, None
