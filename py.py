import psycopg2






conn = psycopg2.connect(host = '127.0.0.1', database = 'postgres', user = 'postgres', password = '123')
cur = conn.cursor()


def prints(cur):
    for i in cur:
        print(i)


def binary(list, find):
    a = 0
    b = len(list) - 1
    while a<b:
        mid = int((a+b)/2)
        if list[mid] == find:
            return mid 
        elif list[mid] < find:
            b = mid 
        elif list[mid] > find:
            a = mid 
    return False



cur.execute("drop table college")
cur.execute("create table if not exists college(id_ serial primary key, name text);")
cur.execute("insert into college(name) values ('john'), ('lube'), ('alzhan')")



cur.execute("SELECT * FROM college order by id_ asc")
namb = [r[0] for r in cur.fetchall()]
cur.execute("SELECT * FROM college order by name asc")
namee = [r[1] for r in cur.fetchall()]


print(namb)



n = int(input('число: '))
print(binary(namb, n))
# print(namee[binary(namb, n)])








while True:
    name = input("введите ваше имя: ")
    if name in namee:
        print('вы еесть в бд')
        break
    else:
        print("сожалею")



prints(namee)

conn.commit()
cur.close()
conn.close()
