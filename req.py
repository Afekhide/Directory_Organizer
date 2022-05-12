import json
import requests
url = 'https://ifconfig.me/all.json'
nssm_url = 'https://nssm.cc/ci/nssm-2.24-101-g897c7ad.zip'

response = requests.get(url)
if response.status_code == 200:
    print((response.json()['ip_addr']))


