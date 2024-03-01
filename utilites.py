import os
import random
import hashlib
from data import db_session
from data.users import User

def get_hash_password(login, password):
    md5_hash = hashlib.new('md5')
    md5_hash.update((login+password).encode())
    key=md5_hash.hexdigest()
    return key


def check_password(login, password):
    hash_input = get_hash_password(login, password)
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()
    if user is not None:
        print(user.name, user.hashed_password)
        if hash_input==user.hashed_password: # Если нашли запись - все ок, пользователь с таким паролем существует
            print('ok')
            return True
    return False

if __name__=="__main__":
    hash = get_hash_password('User', '123')
    check_password('User', '123')