import datetime

from jose import jwt
import secrets
from dotenv import load_dotenv
load_dotenv()
import  os
a =os.getenv('secret_key')






w= jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjA5MzcyMTE2NjgzIiwiZGF0ZSI6IjIwMjMtMDgtMDkgMTE6MzU6MDcifQ.qmcmMPmxFfURIMXiZYpZlQQfxi-rrGLuNNt28L3dG80", a, algorithms=['HS256'])
print(w)




# import hashlib
#
# # Declaring Password
# password = 'GeeksPassword'
# # adding 5gz as password
# salt = "5gz"
#
# # Adding salt at the last of the password
# dataBase_password = password + salt
# # Encoding the password
# hashed = hashlib.md5(dataBase_password.encode())
#
# # Printing the Hash
# print(hashed.hexdigest())