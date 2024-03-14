from random import randint

class Person:
    user_name = 'UserTest'
    email = f'testtetstest123test@test.com'
    password = f'12345Ewq'

class RandomData:
    user_name = 'Test'
    email = f'test{randint(0, 999)}@vk.com'
    password = f'{randint(1000, 9999)}Qwe'