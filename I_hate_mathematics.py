# http://ringzer0team.com/challenges/32

import requests
import re
    
# Authorization by 'username' and 'password'
# Enter your log-in details
URL = 'http://ringzer0team.com/login/'
USERNAME = 'Enter your login here'
PASSWORD = 'Enter your login here'
login_data = {'username':USERNAME,'password':PASSWORD}

my_session = requests.Session()
my_session.post(URL, data=login_data)

page_task = my_session.get('http://ringzer0team.com/challenges/32')
# print page_task.content

# Carve a 3 values for calculation
message = re.findall(re.compile('----- BEGIN MESSAGE -----<br />[\r\n\s]*(\d+?)\s+\+\s+(0x[a-f\d]+?)\s+-\s+(\d+)\s+='), page_task.text)
# message_ascii = binascii.unhexlify('%x' % int(message_bin[0], 2))
(first_summand_dec, second_summand_hex, third_summand_bin) = message[0]
# print first_summand_dec, second_summand_hex, third_summand_bin
first_summand_dec, second_summand_hex, third_summand_bin = int(first_summand_dec), int(second_summand_hex, 16), int(third_summand_bin, 2)
# print first_summand_dec, second_summand_hex, third_summand_bin
answer = first_summand_dec + second_summand_hex - third_summand_bin
# print answer

# Send our answer to server
page_answer = my_session.get('http://ringzer0team.com/challenges/32/' + str(answer))
# print page_answer.content

# Get final flag from response page
my_flag = 'FLAG-' + re.findall('<div class="alert alert-info">FLAG-(.+?)</div>', page_answer.text)[0]
print my_flag

# my_flag - that's your flag, which you have to submit
