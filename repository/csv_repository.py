import csv
import os
from datetime import datetime
from database.connect import my_collection, days_sum, month_sum

def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row


def init_car_accident():
   my_collection.drop()
   days_sum.drop()
   month_sum.drop()
   x = 0
   for row in read_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'Traffic_Crashes_-_Crashes - 20k rows.csv')):

        row['CRASH_DATE'] = row['CRASH_DATE'][:10]
        row['CRASH_DATE'] = datetime.strptime(row['CRASH_DATE'], '%m/%d/%Y')

        accident = {
           "date": row['CRASH_DATE'],
           "region": row["BEAT_OF_OCCURRENCE"],
           "main_cause": row["PRIM_CONTRIBUTORY_CAUSE"],
           "injuries":{
               'total': safe_int(row['INJURIES_TOTAL']),
               'fatal': safe_int(row['INJURIES_FATAL']),
               'non_fatal': safe_int(row['INJURIES_TOTAL']) - safe_int(row['INJURIES_FATAL'])
           }
        }
        my_collection.insert_one(accident)

        query_day = {'date': row['CRASH_DATE'], 'region': row['BEAT_OF_OCCURRENCE']}
        update_day = {'$inc': {'count': 1}}
        days_sum.update_one(query_day, update_day, upsert=True)

        query_month = {'date.month': row['CRASH_DATE'].month, 'date.year': row['CRASH_DATE'].year,
                       'region': row['BEAT_OF_OCCURRENCE']}
        update_month = {'$inc': {'count': 1}}
        month_sum.update_one(query_month, update_month, upsert=True)


def safe_int(value):
    try:
        return int(value)
    except Exception:
        return 0