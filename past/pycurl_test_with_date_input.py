import pycurl
import urllib

c = pycurl.Curl()

#example of taking a string input from terminal and making it into date-time object
last_seen_date_input = raw_input("Enter last seen date (valid format is YYYY-MM-DD): ")
last_seen_date = datetime.strftime( datetime.strptime(str(lastSeenDateInput), '%Y-%m-%d'), '%Y-%m-%d')

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

