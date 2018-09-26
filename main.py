import requests
try:
	r = requests.get('https://somesite.com', verify=True)

except requests.exceptions.SSLError:
    print "bad SSL"

except Exception as e:
	print "Unknown error"
