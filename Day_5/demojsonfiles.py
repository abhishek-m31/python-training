import json

try:
    with open('../Day_5/files/employee.json', 'r') as fr:
        data = json.load(fr)
        print(data)
        print(f'Name: {data["Name"]}, Age : {data["Age"]}, Department : {data["Dept"]}')
        skills = data["skills"]
        for skill in skills:
            print(f'{skill["Title"]}, {skill["Exp"]}')
except FileNotFoundError as er:
    print(er) 

print('-----------------------------------')
booking_data = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"

}     

try:
    with open('../Day_5/files/bookings.json', 'w') as fw:
        json.dump(booking_data, fw, indent = 4)
except FileNotFoundError as er:
    print(er)        

print('--------------------------')
booking = json.dumps(booking_data)
print(booking)

print('--------------------------')
json_booking = json.loads(booking)  #string t json
print(json_booking)

