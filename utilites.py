import os
import hashlib

salt = os.urandom(32)


def get_hash_password(login, password):
    salt = os.urandom(32)  # Запомните
    key = hashlib.pbkdf2_hmac(
        'sha256',  # Используемый алгоритм хеширования
        password.encode('utf-8'),  # Конвертируется пароль в байты
        salt,  # Предоставляется соль
        100000)  # Рекомендуется использовать хотя бы 100000 итераций SHA-256
    return key


def check_password(login, password):
    hash_input = get_hash_password(login, password)
    # Ищем в БД запись о пользователе с таким хешем
    if 1==1: # Если нашли запись - все ок, пользователь с таким паролем существует
        return True
    return False

if __name__=="__main__":
    hash = get_hash_password('User', '123')
    check_password('User', '123')