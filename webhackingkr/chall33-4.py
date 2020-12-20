import requests
import hashlib
import time
from math import ceil

import webbrowser

url = 'https://webhacking.kr/challenge/bonus-6/l4.php?password='
cookies = {'PHPSESSID': ''}

enc = hashlib.md5(str(ceil(time.time())).encode())
encTxt = enc.hexdigest()

print(time.time(), encTxt)

# r = requests.get(url+encTxt, cookies=cookies)
webbrowser.open_new_tab(url+encTxt)

# print(r.text, r.url)
