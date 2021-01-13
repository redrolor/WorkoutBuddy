import hashlib
import random
from base64 import b64encode
import datetime
import requests

def getStudentInfo(id):
    url = 'https://tigerbook.herokuapp.com/api/v1/undergraduates/' + id
    created = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    nonce = ''.join([random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=') for i in range(32)])
    username = 'vkonuru'
    password = '858e9b714dd2088b1d26f22077f09986'

    generated_digest = b64encode(hashlib.sha256((nonce + created + password).encode('utf-8')).digest()).decode('utf-8')

    r = requests.get(url, headers = {
        'Authorization': 'WSSE profile="UsernameToken"',
        'X-WSSE': 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s"' % (username, generated_digest, b64encode(nonce.encode()).decode('utf-8'), created)
    })
    return r.json()
