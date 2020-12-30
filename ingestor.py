import psycopg2
import datetime


conn = psycopg2.connect(database="recipe_book", user="postgres", password="admin", host="127.0.0.1", port="5432")
print ("Opened database successfully")

cur = conn.cursor()

# cur.execute("INSERT INTO food (id,country,state,zone,dishes,rating,file_name,created_date) \
#       VALUES (1, 'IND','KA', 'South','Idli', 3, '','30-DEC-20')")

# conn.commit()
# print ("Records created successfully")
# conn.close()

country = ['IND']
food = [['KA','South',['Dosa','Rasam','Pongal']], 
         ['TA','South',['Rasam','']],
         ['JHD','East',['Malpua','Dhuska','Litti Chokha']],
         ['WB','East',['Fish','Rosogullas','Sondesh']],
         ['Rajasthan','North',['Dal baati churma','Gatte ki subzi','Ker sangri']],
         ['Panjab','North',['Butter Chicken','Chole Bhature','Makkey Di Roti']],
         ['Gujarat','West',['Dhokla','Khandvi','Thepla']],
         ['Maharashtra','West',['Puran Poli','Vada Paw']]
         ]


i = 2
for con in country:
        for fd in food:
            print(fd)
            for ds in fd[2]:
                # xx = 0
                # print("{} - {} - {} - {}".format(con, fd[0], fd[1], ds))
                cur.execute("INSERT INTO food (id,country,state,zone,dishes,rating,file_name,created_date) VALUES ({}, '{}','{}', '{}','{}', 3, '','{}')".format(i,con, fd[0],fd[1],ds,datetime.datetime.now()))
                conn.commit()
                i += 1

conn.close()
    