import requests

url = 'https://www.terrybu.com'
data = {
  "AccountHolderPhoneNumber": "1234"
}
response = requests.post(url, data=data)
print(response.text)

print(response)