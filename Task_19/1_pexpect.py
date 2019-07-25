import pexpect
import getpass
import sys

COMMAND = sys.argv[1]
USER = input('Username: ')
PASSWORD = getpass.getpass()
ENABLE_PASS = getpass.getpass(prompt='Enter enbale password: ')

DEVICES_IP = ['10.0.1.68']

for IP in DEVICES_IP:
	print('Connection to device {}'.format(IP))
	with pexpect.spawn('ssh {}@{}'.format(USER, IP)) as ssh:

		ssh.expect('Password:')
		ssh.sendline(PASSWORD)

		ssh.expect('[#>]')
		ssh.sendline('enable')

		ssh.expect('#')
		ssh.sendline('terminal length 0')

		ssh.expect('#')
		ssh.sendline(COMMAND)

		ssh.expect('#')
		print(ssh.before.decode('utf-8'))

