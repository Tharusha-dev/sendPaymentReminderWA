from twilio.rest import Client
import json
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import re



ACCOUNT_SID = ''
AUTH_TOKEN = ''

DATABASE_NAME = ''


NEXT_PAYMENT_DATE_FILED = ''
PAYMENT_AMOUNT_FIELD = ''


URI = ''


mongo_client = MongoClient(URI, server_api=ServerApi('1'))
db = mongo_client[DATABASE_NAME]
collection = db.installment_orders


twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)

try:
    mongo_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

    
today_with_time = requests.get("http://worldtimeapi.org/api/timezone/").json()['datetime']


def set_to_midnight(date):
    pattern_of_time = r'\d{2}:\d{2}:\d{2}'
    date_list = date.split(".")[0]
    new_date = re.sub(pattern_of_time,"00:00:00",date_list)

    new_date2 = datetime.strptime(new_date,'%Y-%m-%dT%H:%M:%S')  

    print(f'processed date {new_date2}')

    return new_date2

today_set_to_midnight = set_to_midnight(today_with_time)



customer_with_payment_due = collection.find({'next_payment_datetime_local':today_set_to_midnight})

for customer in customer_with_payment_due:
    print(customer)
    customer_wa = customer['customer_wa']
    payment = customer['monthly']
    prod_name = customer['prod_name']
    message = twilio_client.messages.create(
                              content_sid='HXXXXXX',
                              from_='MGXXXXXXX',
                              content_variables=json.dumps({
                                  '1': str(payment),
                                  '2': prod_name
                              }),
                              to=f'whatsapp:{customer_wa}')



