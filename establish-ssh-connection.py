#import modules
import pexpect

#define variables
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'

#create ssh connection---#auto accept ssh keys = ssh -o "StrictHostKeyChecking 0" 
session = pexpect.spawn('ssh -o "StrictHostKeyChecking 0" ' + username + '@' + ip_address,encoding='utf-8', timeout=20)
result = session.expect(['Password:',pexpect.TIMEOUT,pexpect.EOF])

#check for error, if exists then display and exit
if result != 0:
    print('-'*3,'FAILURE! creating session for: ', ip_address)
    exit()

#session expecting password, enter details
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT,pexpect.EOF])

#check for error, if exists then display and exit
if result != 0:
    print('-'*3,'FAILURE! entering password: ', password)
    exit()

#enter enable mode
session.sendline('enable')
result = session.expect(['Password:',pexpect.TIMEOUT,pexpect.EOF])

#check for error, if exists then display and exit
if result != 0:
    print('-'*3,'FAILURE! entering enable mode')
    exit()

#send enable password details 
session.sendline(password_enable)
result = session.expect(['#',pexpect.TIMEOUT,pexpect.EOF])

#check for error, if exists then display and exit
if result != 0:
    print('-'*3,'FAILURE! entering enable mode after sending password')
    exit()
    
#enter config mode
session.sendline('configure terminal')
result = session.expect([r'.\(config\)#', pexpect.TIMEOUT,pexpect.EOF])

#check for error, if exists then display and exit
if result != 0:
    print('-'*3,'FAILURE! entering config mode')
    exit()

#change hostname to R1
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#',pexpect.TIMEOUT,pexpect.EOF])

#check for error, if exists then display and exit
if result != 0:
    print('-'*3,'FAILURE! setting hostname')
    exit()

#exit config mode
session.sendline('exit')

#exit enable mode
session.sendline('exit')

#display success message
print('-'*25)
print('')
print('-'*3, 'Success! connecting to: ',ip_address)
print('-'*3,               'Username: ',username)
print('-'*3,               'Password: ',password)
print('-'*25)

#terminate ssh session
session.close()
