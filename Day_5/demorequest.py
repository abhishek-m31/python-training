import json
import requests as req

response = req.get('https://reqres.in/api/users?page=2')
print(response.status_code)
print('application/json' in response.headers['Content-Type'])
response_data = json.loads(response.text)
print(response_data)
data = response_data['data']
for records in data:
    if records['id'] == 7:
        if records['first_name'] == 'Michael':
            print('record matched') 