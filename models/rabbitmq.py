import datetime

import pika
import json
from database.mongodb import sms_db
from instance.server import Name


class Instance:
    sms = 'sms'
    history = 'history'
    Rabbit_pass = 'guest'
    Rabbit_user = 'guest'
    port = 5672
    host = '172.19.0.3'


class RaabbitMQ:
    def __init__(self):
        credentials = pika.PlainCredentials(Instance.Rabbit_user, Instance.Rabbit_pass)

        parameters = pika.ConnectionParameters(Instance.host,
                                               Instance.port,
                                               '/',
                                               credentials)
        connection = pika.BlockingConnection(parameters)
        self.channel = connection.channel()

    def send_sms(self, data: json = None) -> bool:
        user_data = json.loads(data)
        count = sms_db.find_one({
            Name.phone: str(user_data[Name.phone]),

        })

        time_diff = 150
        if count is not None:
            time: datetime.datetime = count.get(Name.date)
            time_diff = (datetime.datetime.now() - time).seconds

        if time_diff > 120:
            self.channel.queue_declare(queue=Instance.sms)
            self.channel.basic_publish(exchange='', routing_key=Instance.sms, body=data)
            self.channel.close()
            return True
        else:
            return False
