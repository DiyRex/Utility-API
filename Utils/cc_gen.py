import datetime
import random
import string
from datetime import datetime

def random_card(amount):
    for i in range(amount):
        bin_length = len(bin)
        needed_length = 16 - int(bin_length)
        rest_card_number = ''.join(
            random.choices(string.digits, k=needed_length))
        card_number = bin + rest_card_number
        mon = random.randint(1, 12)
        month = str(mon).zfill(2)
        current_year = datetime.now().year
        year = random.randint(current_year + 2, current_year + 5)
        ccv = random.randint(100, 999)
        hit = card_number + "|" + month + "|" + str(year) + "|" + str(ccv)
        print(hit)


def rnd_year():
    current_year = datetime.now().year
    year = random.randint(current_year + 2, current_year + 5)
    return year


def rnd_month():
    mon = random.randint(1, 12)
    month = str(mon).zfill(2)
    return month


def rnd_ccv():
    ccv = random.randint(000, 999)
    return f"{ccv:03d}"


def generate_card(bin, year, month, ccv):
    bin_length = len(bin)
    needed_length = 16 - int(bin_length)
    rest_card_number = ''.join(random.choices(string.digits, k=needed_length))
    card_number = bin + rest_card_number
    if year == "rnd":
        year = rnd_year()
    else:
        pass
    if month == "rnd":
        month = rnd_month()
    else:
        pass
    if ccv == "rnd":
        ccv = rnd_ccv()
    else:
        pass
    hit = card_number + "|" + month + "|" + str(year) + "|" + str(ccv)
    return hit




def generate_cards(amount,bin, year, month, ccv):
    card_list = []
    for i in range(20):
        card = generate_card(bin=bin, year=year, month=month, ccv=ccv)
        card_list.append(card)
    return card_list

def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False

# cards = generate_cards(bin="4324534", year="rnd", month="rnd", ccv="rnd",amount=20)
def valid_cards(amount,bin, year, month, ccv):
    checked = []
    while True:
        card = generate_card(bin=bin, year=year, month=month, ccv=ccv)
        checked.append(card)
        if len(checked) == amount:
            break
    return checked
 