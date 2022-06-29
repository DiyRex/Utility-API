import requests
import json
from bs4 import BeautifulSoup

def fake_profile():

    response = requests.get("https://www.fakepersongenerator.com/")
    soup = BeautifulSoup(response.text,"html.parser")

    name = soup.find_all('b')[0].text.replace(u'\xa0', ' ')
    gend = soup.find_all('b')[1].text
    race = soup.find_all('b')[2].text
    birthday = soup.find_all('b')[3].text
    age = soup.find_all('b')[4].text
    addr_street = soup.find_all('b')[5].text
    addr_state = soup.find_all('b')[6].text
    address = f"{addr_street},{addr_state}"
    tele = soup.find_all('b')[7].text
    mobile = soup.find_all('b')[8].text
    ssn = soup.find_all('input', attrs={'class':'form-control'})[11].get('value')


    profile = str({"Name":name, "Gender":gend, "Race":race, "Birthday":birthday, "Age":age, "Address":address, "Telephone":tele, "Mobile":mobile, "SSN":ssn})
    return profile