# http://ringzer0team.com/challenges/121

import requests
import re
import hashlib
import os

# Authorization by 'username' and 'password'
# Enter your log-in details
URL = 'http://ringzer0team.com/login/'
USERNAME = 'Enter your login here'
PASSWORD = 'Enter your login here'
login_data = {'username':USERNAME,'password':PASSWORD}

my_session = requests.Session()
my_session.post(URL, data=login_data)

page_task = my_session.get('http://ringzer0team.com/challenges/121')
# print page_task.content

# Carve a shellcode
message_shellcode = re.findall(re.compile('----- BEGIN SHELLCODE -----<br />[\r\n\s]*(.+?)[\r\n\s]*<br />'), page_task.text)
# print message_shellcode[0]

# Write a program with shell script
c_prog_with_shell = '#include <unistd.h>\nchar code[] = \"' + message_shellcode[0] + '\";\nint main(int argc, char **argv){\nint (*func)();\nfunc = (int (*)()) code;\n(int)(*func)();\nreturn 0;\n}' 
f = open('c_prog_with_shell.c','wb')
f.write(c_prog_with_shell)
f.close()

# Execute program and shell script
os.system("gcc -g c_prog_with_shell.c -o test")
os.system("execstack -s test")
os.system("script -c ./test")

f=open('typescript','r')
f.readline()
answer = f.readline()
# print answer[0:-1]

# Send our hash to server
page_answer = my_session.get('http://ringzer0team.com/challenges/121/' + answer[0:-1])
# print page_answer.content

# Get final flag from response page
my_flag = 'FLAG-' + re.findall('<div class="alert alert-info">FLAG-(.+?)</div>', page_answer.text)[0]
print my_flag

# my_flag - that's your flag, which you have to submit
