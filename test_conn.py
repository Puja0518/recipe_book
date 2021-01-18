import requests

url =  "http://127.0.0.1:9000/login"
payload = {
    "email": "xyz@mail.com",
    "password": "testpassword"
}
r = requests.post(url, json=payload)
print(r.status_code)
print(r.text)
