# http://ringzer0team.com/challenges/56

import requests
import re
import hashlib

# Create list with hashes of numbers
hash_table_1000 = [hashlib.sha1(str(x)).hexdigest() for x in range(10000)]

# Authorization by 'username' and 'password'
# Enter your log-in details
URL = 'http://ringzer0team.com/login/'
USERNAME = 'Enter your login here'
PASSWORD = 'Enter your login here'
login_data = {'username':USERNAME,'password':PASSWORD}

my_session = requests.Session()
my_session.post(URL, data=login_data)

page_task = my_session.get('http://ringzer0team.com/challenges/56')
# print page_task.content

# Carve a message for hashing
message_hash = re.findall(re.compile('----- BEGIN HASH -----<br />[\r\n\s]*(.+?)[\r\n\s]*<br />'), page_task.text)
# print message_hash

message_answer = hash_table_1000.index(str(message_hash[0]))
# print message_answer

# Send our answer to server
page_answer = my_session.get('http://ringzer0team.com/challenges/56/' + str(message_answer))
# print page_answer.content

# Get final flag from response page
my_flag = 'FLAG-' + re.findall('<div class="alert alert-info">FLAG-(.+?)</div>', page_answer.text)[0]
print my_flag

# my_flag - that's your flag, which you have to submit


