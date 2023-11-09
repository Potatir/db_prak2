import psycopg2






conn = psycopg2.connect(host = '127.0.0.1', database = 'postgres', user = 'postgres', password = '123')
cur = conn.cursor()


def prints(cur):
    for i in cur:
        print(i)


cur.execute("SELECT * FROM college")
namee = [r[1] for r in cur.fetchall()]
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
