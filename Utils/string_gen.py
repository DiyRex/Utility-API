import random
import string

def adv_password(amount,length):
    pw_list = []
    for i in range(amount):
        pwd = ''.join(random.choice(string.ascii_uppercase+string.digits+string.ascii_lowercase)for p in range(length))
        pw_list.append(pwd)
    return pw_list

# print(adv_password(amount=100,length=10))

