import requests

num = input("Enter phone number: ")
print(num)
url = ''
data = {
  
}
response = requests.post(url, data=data)

print("***Response Object***")
print(response)
print("***Response Text***\n" + response.text)
