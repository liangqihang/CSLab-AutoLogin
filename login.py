import requests
import argparse

parser = argparse.ArgumentParser(description='CSLab Login')
parser.add_argument('--eid', metavar='N', type=str, help='CityU EID')
parser.add_argument('--pwd', metavar='N', type=str, help='CityU password')
args = parser.parse_args()

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://cp.cs.cityu.edu.hk:16979',
    'Connection': 'keep-alive',
    'Referer': 'https://cp.cs.cityu.edu.hk:16979/loginform.html?',
    'Upgrade-Insecure-Requests': '1',
}
data = {
  'username': args.eid,
  'ctx_pass': args.pwd,
  'domain_name': 'CITYUMD',
  'modify': 'Secure Login'
}

response = requests.post('https://cp.cs.cityu.edu.hk:16979/loginform.html', headers=headers, data=data)