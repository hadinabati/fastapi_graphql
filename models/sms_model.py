import random
from schema.register_schema import Error, SMS
from typing import Union
from instance.error_instance import Error as ErrorInstance
from instance.server import Name
import json
from models.rabbitmq import RaabbitMQ


class Sms:
    def __init__(self, mobile: str):
        self.mobile = mobile

    def send(self, message: str):
        pass

    def otp(self) -> Union[Error, SMS]:
        # search in db that it has been sended yet
        number = random.randint(a=1000, b=9999)
        message = 'کاربر گرامی کد تاییده شما  : '
        text = message + '\n' + str(number) + "\n"
        try:
            data = {
                Name.phone : self.mobile,
                Name.number: number,
                Name.text: text
            }
            data = json.dumps(data)
            cl = RaabbitMQ()
            res = cl.send_sms(data=data)
            if res:
                return SMS(type='otp', message='ارسال با موفقیت انجام شد')
            else:
                return Error(error_code=ErrorInstance.SMS.code_2001, message_code=ErrorInstance.SMS.message_2001)
        except IndexError:
            return Error(error_code=ErrorInstance.SMS.code_2000, message_code=ErrorInstance.SMS.message_2000)
