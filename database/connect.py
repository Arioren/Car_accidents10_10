from pymongo import MongoClient


client = MongoClient('mongodb://172.21.89.32:27017')
car_accident_db = client['car_accident']


my_collection = car_accident_db['drivers']

days_sum = car_accident_db['days_sum']
month_sum = car_accident_db['month_sum']