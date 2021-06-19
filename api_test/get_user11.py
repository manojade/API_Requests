import requests

resp = requests.get("https://reqres.in/api/users?page=2")

json_response = resp.json()

total = json_response['total']
assert total == 12

total_pages = json_response['total_pages']
assert total_pages == 2

data = json_response['data'][0]['email']
print(data)
assert data == 'michael.lawson@reqres.in', 'email is not matched'
flag = data.__contains__('michael')
print(flag)
assert flag