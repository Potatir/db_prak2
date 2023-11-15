import psycopg2
import csv



conn = psycopg2.connect(database = 'postgres', user = 'postgres', password = '123',port = '5432')
cur = conn.cursor()
cur.execute('SELECT * FROM country limit 10')
gg = cur.fetchall()
for i in gg:
    print(i)

csvfile = open('output.csv', 'w') 
csvwriter = csv.writer(csvfile)
for row in gg:
    csvwriter.writerow(row)











# conn = psycopg2.connect(host = '127.0.0.1', database = 'postgres', user = 'postgres', password = '123')
# cur = conn.cursor()


# def prints(cur):
#     for i in cur:
#         print(i)


# def binary(lis, fin):
#     a = 0
#     b = len(lis) -1
#     while a<=b:
#         mid = int((a+b)//2)
#         input((a, b, mid))
#         if lis[mid] == fin:
#             return mid 
#         elif lis[mid] > fin:
#             b = mid - 1
#         elif lis[mid] < fin:
#             a = mid + 1
#         input((a, b, mid))
#     return False



# cur.execute("drop table if exists college")
# cur.execute("create table if not exists college(id_ serial primary key, name text);")
# cur.execute("insert into college(name) values ('john'), ('lube'), ('alzhan'),('gg'),('aa')")
# conn.commit()


# cur.execute("SELECT * FROM college order by id_ asc")
# namb = [r[0] for r in cur.fetchall()]
# cur.execute("SELECT * FROM college order by name asc")
# namee = [r[1] for r in cur.fetchall()]


# print(namb)



# n = int(input('число: '))
# print(binary(namb, n))
# # print(namee[binary(namb, n)])








# # while True:
# #     name = input("введите ваше имя: ")
# #     if name in namee:
# #         print('вы еесть в бд')
# #         break
# #     else:
# #         print("сожалею")



# # prints(namee)

# conn.commit()
# cur.close()
# conn.close()
