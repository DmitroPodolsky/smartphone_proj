import random


def generate_password():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 8
    for n in range(1):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        return password
