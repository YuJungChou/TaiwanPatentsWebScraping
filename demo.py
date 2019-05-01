#%%
import os, sys
import re
import json
import requests
import time, datetime
from bs4 import BeautifulSoup
import random

'''
url = 'https://twpat-simple.tipo.gov.tw/tipotwoc/tipotwkm?@@'+\
        str(random.randint(1,25600))
url_head = os.path.dirname(url)
url_tail = os.path.basename(url)

headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
req = requests.get(url, headers = headers)
req.encoding = req.apparent_encoding #req.encoding = 'big5-hkscs'
bs = BeautifulSoup(req.text, 'html.parser')
'''