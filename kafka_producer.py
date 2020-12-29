from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


from nsepy.history import get_price_list
from datetime import date

for i in range(15,26,1):
    print(i)
    try:
        prices = get_price_list(dt=date(2020,9,i))
        records - prices.to_dict('records')
        for rec in records:
            producer.send('stocks', value=rec)
            

    except:
        print("NO DATA FOUND ON {} DECEMBER ".format(i))