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
food = [ ['AP','South',['Punugulu','Gutti Vankaya Kura','Kodi Pulao']], 
         ['kerala','South',['Puttu','Appam','Idiyappam','Banana Halwa']],
         ['Odisha','East',['Khicede','Dalma','Pakhala Bhata','Chhena Poda']],
         ['Bihar','East',['Chandrakala/ Pedakiya','Khaja','Reshmi Kebabs','Mutton Kebabs','Dal Peetha','Thekua']],
         ['J&K','North',['Rogan Josh','Kachaloo Chaat','Kaladi Kulcha','Kashmiri Polao','Seekh Kebab']],
         ['UP','North',['Boti Kabab','Chilla','Chicken Biryani']],
         ['Delhi','North',['Paranthas','Golgappe','Rabri Faluda','Bhel Puri','Pav Bhaji','Dabeli','Momos']],
         ['Goa','West',['Goan Fish Curry','Chicken Cafreal','Sorak','Samarachi Kodi']]
        ]


i = 24
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
    