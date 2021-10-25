# github factorio changelog/version parser?

from typing import Pattern
import requests, re

url = 'https://raw.githubusercontent.com/wube/factorio-data/master/changelog.txt'
c = requests.get(url=url)
data = c.text
c.close()

temp = []

pattern = re.compile(r'(?=Version:).*\n(Date:).*\n')
iter = re.finditer(pattern, data)

for m in iter:
    res = m.group().splitlines()
    v = res[0][9:]
    d = res[1][6:]
    
    temp.append((v, d))

print(temp)

