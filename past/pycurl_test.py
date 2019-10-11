import pycurl
import urllib

c = pycurl.Curl()

url = 'https://www.terrybu.com'

post_params = [
    ('AccountHolderPhoneNumber','2126468082'),
]
resp_data = urllib.urlencode(post_params)

c.setopt(pycurl.POSTFIELDS, resp_data)
c.setopt(c.URL, url)
c.perform()
print("\n\nRESPONSE CODE: " + str(c.getinfo(pycurl.HTTP_CODE)))
print(c.getinfo(pycurl.EFFECTIVE_URL))

c.close()

