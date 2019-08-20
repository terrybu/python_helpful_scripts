# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://oapi.payfone.com/identity/:phoneNumber/verify/v1"
  
# defining a params dict for the parameters to be sent to the API 
params = {} 
token = ''
headers = {'content-type': 'application/json', 'Authorization': 'Bearer {}'.format(token)}

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = params, headers=headers) 
  
# extracting data in json format 
data = r.json() 

print(data)