import csv
import os

from database.connect import my_collection

def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row


def init_car_accident():
   my_collection.drop()

   for row in read_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'Traffic_Crashes_-_Crashes - 20k rows.csv')):
