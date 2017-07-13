import bcrypt


def encrypt(password, salt=None):
    return bcrypt.hashpw(password.encode('utf-8'), salt if salt else bcrypt.gensalt())


def decrypt(password, hashed):
    if bcrypt.hashpw(password.encode('utf-8'), hashed.encode('utf-8')) == hashed.encode('utf-8'):
        return True
    else:
        return False
