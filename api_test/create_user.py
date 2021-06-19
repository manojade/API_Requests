import json

import requests

'''payload = {
    "name": "morpheus",
    "job": "leader"
       }
print(type(payload))

requests.post("https://reqres.in/api/users",data=payload)'''

jsonData = open("data.json", 'r').read()

resp = requests.post("https://reqres.in/api/users", data = json.loads(jsonData))
#resp = requests.post("https://reqres.in/api/users", data = json.loads(open("data.json", "r").read()))

print(resp)
print(resp.json())
assert resp.json()['job'] == 'leader'
