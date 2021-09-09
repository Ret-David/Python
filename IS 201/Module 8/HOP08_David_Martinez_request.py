# David Martinez

import requests

res = requests.get('http://web.textfiles.com/computers/3dbasics.txt')

try:
    res.raise_for_status()
    print("Status Code: ", res.status_code)
    print("Length of the text: ", len(res.text))
    print(res.text[:103])   # splice how much text you wish to retrieve [start:stop]
except Exception as exc:
    print("Oh no: %s" %(exc))


# ====== Results from above ======
# Status Code:  200
# Length of the text:  6905
# Basic Introduction to 3D Programming
# By Synergist
#
# Ok, this is NOT fun. Not at all and I'm sure any
