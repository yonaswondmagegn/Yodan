import os
import random
import string
import requests    
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('AFRO_SMS_KEY')

session = requests.Session()
base_url = 'https://api.afromessage.com/api/challenge'

def generate_random_text():
    characters = list(string.digits +string.ascii_letters + str(string.punctuation))
    random.shuffle(characters)
    return ''.join(characters[:16])


def send_otp(phonenumber):
    headers = {'Authorization': 'Bearer ' + token}
    to = phonenumber
    pre = "Your Zion Verification Code is"
    post = "Thanks Being Part Of Us"
    sb = 1
    sa = 1
    ttl = 0
    len = 4
    t = 0
    # final url
    url = '%s?from=&sender=&to=%s&pr=%s&ps=%s&callback=&sb=%d&sa=%d&ttl=%d&len=%d&t=%d' % (base_url,  to, pre, post,  sb, sa, ttl, len, t)
    # make request
    result = session.get(url, headers=headers)
    # check result
    if result.status_code == 200:
        # request is success. inspect the json object for the value of `acknowledge`
        json = result.json()
        if json['acknowledge'] == 'success':
            print(json)
            return json['response']
        else:
            return ValueError('Some Thing Went Wrong can not send the OTP')
    else:
        # anything other than 200 goes here.
        print ('http error ... code: %d , msg: %s ' % (result.status_code, result.content) )
        return ValueError('Some Thing Went Wrong can not send the OTP')
