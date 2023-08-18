import datetime

import pika
import requests
import json
from instance.server import Name
from models.rabbitmq import Instance
from database.mongodb import sms_db


def main():
    credentials = pika.PlainCredentials(Instance.Rabbit_user, Instance.Rabbit_pass)

    parameters = pika.ConnectionParameters(Instance.host,
                                           Instance.port,
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue=Instance.sms)
    channel.basic_consume(queue=Instance.sms, on_message_callback=send_sms_callback, auto_ack=True)

    channel.start_consuming()


def send_sms_callback(h, method, properties, body):
    url = "http://sms.parsgreen.ir/UrlService/sendSMS.ashx"
    data = json.loads(body)
    number = data[Name.number]
    phone = data[Name.phone]
    sms_db.insert_one({
        Name.phone: phone,
        Name.number: number,
        Name.date: datetime.datetime.now()
    })
    message = data[Name.text]
    requests.get(url=url, params={
        "from": "10001398",
        'to': phone,
        'text': message,
        'signature': 'B7C9B5C7-B3F5-4E59-A892-23CA581AA424'
    })


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Error Running rabbitMq receiver')
