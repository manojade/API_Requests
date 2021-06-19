import requests

p = {"page":2}

resp = requests.get("https://reqres.in/api/users",params=p)
# resp = requests.get("https://reqres.in/api/users?page=2")

code = resp.status_code

assert code == 200, "code doesn't match"

#print(resp.text)
#print(resp.content)
print(resp.json())
print(type(resp.headers))
print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)

