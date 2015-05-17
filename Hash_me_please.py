# http://ringzer0team.com/challenges/13

import requests
import re
import hashlib

# Authorization by 'username' and 'password'
# Enter your log-in details
URL = 'http://ringzer0team.com/login/'
USERNAME = 'Enter your login here'
PASSWORD = 'Enter your login here'
login_data = {'username':USERNAME,'password':PASSWORD}

my_session = requests.Session()
my_session.post(URL, data=login_data)

page_task = my_session.get('http://ringzer0team.com/challenges/13')
# print page_task.content

# Carve a message for hashing
message = re.findall(re.compile('----- BEGIN MESSAGE -----<br />[\r\n\s]*(.+?)[\r\n\s]*<br />'), page_task.text)
# print message[0]
# Get a hash from message
message_hash = hashlib.sha512(message[0])
# print message_hash.hexdigest()

# Send our hash to server
page_answer = my_session.get('http://ringzer0team.com/challenges/13/' + message_hash.hexdigest())
# print page_answer.content

# Get final flag from response page
my_flag = 'FLAG-' + re.findall('<div class="alert alert-info">FLAG-(.+?)</div>', page_answer.text)[0]
print my_flag

# my_flag - that's your flag, which you have to submit
