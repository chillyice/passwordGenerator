from hashlib import md5


#  获取原始密码+salt的md5值
def encrypt_md5_with_salt(passwd, salt):
    md5_obj = md5()
    md5_obj.update((passwd + salt).encode('utf-8'))
    return md5_obj.hexdigest()


if __name__ == '__main__':
    pwd = '123456'
    salt = 'ice'
    print(encrypt_md5_with_salt(pwd, salt))
