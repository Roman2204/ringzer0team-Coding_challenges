# http://ringzer0team.com/challenges/57

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

page_task = my_session.get('http://ringzer0team.com/challenges/57')
# print page_task.content

# Carve a hash and its salt
message = re.findall(re.compile('----- BEGIN HASH -----<br />[\r\n\s]*(.+?)[\r\n\s]*<br />[\s\S]+?----- BEGIN SALT -----<br />[\r\n\s]*(.+?)<br />'), page_task.text)
# print message
message_hash = message[0][0]
message_salt = message[0][1]
# print message_hash
# print message_salt

# Create list with hashes of numbers with message_salt
hash_table_1000_with_salt_after = [hashlib.sha1(str(x) + str(message_salt)).hexdigest() for x in range(10000)]

message_answer = hash_table_1000_with_salt_after.index(str(message_hash))
# print message_answer

# Send our answer to server
page_answer = my_session.get('http://ringzer0team.com/challenges/57/' + str(message_answer))
# print page_answer.content

# Get final flag from response page
my_flag = 'FLAG-' + re.findall('<div class="alert alert-info">FLAG-(.+?)</div>', page_answer.text)[0]
print my_flag

# my_flag - that's your flag, which you have to submit
