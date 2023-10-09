from netmiko import ConnectHandler
from datetime import datetime
import getpass
import sys
import os

now = datetime.now()
scriptTime = now.strftime('%H-%M-%S')

cmds = []
skipped = []

def run_cmd_print(device, commands):
    try:
        sshConnect = ConnectHandler(**device)
        sshConnect.enable()  # Enter enable mode (if needed)
        for command in commands:
            output = sshConnect.send_command(command)
            with open(f'checks{scriptTime}.txt', 'a') as outputText:
                outputText.write('-' * 10 + device.get('ip', 'NOTFOUND') + ' ' + command + '-' * 10 + '\n')
                print("-" * 25 + device.get('ip', 'NOTFOUND') + '-' + command + '-' * 25)
                print(output)
                outputText.write(output + '\n')
                print("-" * 50)
        sshConnect.disconnect()
    except Exception as e:
        print(device.get('ip', 'NOTFOUND') + f' Failed to connect: {str(e)}')
        skipped.append(device.get('ip', 'NOTFOUND'))

username = os.getlogin()
print(f'Running as local user ({username})')

password = getpass.getpass('Please enter your password: ')

enable_mode = input('Do you need to enter enable mode? [y/n]: ')

if enable_mode.lower() == 'y':
    enable_password = getpass.getpass('Enter the enable password: ')
else:
    enable_password = None

switches = []

print('This script will connect to the following hosts:')

try:
    with open('hosts.txt') as hostsFile:
        for line in hostsFile:
            switchAdd = line.strip()
            switchDic = {
               'device_type': 'cisco_ios',
               'ip': switchAdd,
               'username': username,
               'password': password,
               'secret': enable_password,  # Use the entered enable password
               'port': '22',
            }
            switches.append(switchDic)
            print(switchAdd)
except FileNotFoundError:
    print('Hosts file not found. Please create a file called \'hosts.txt\' in the same directory as this script and run again.')
    quit()

print('And run the following commands on each host:')

try:
    with open('commands.txt') as commandsFile:
        for line in commandsFile:
            commandAdd = line.strip()
            cmds.append(commandAdd)
            print(commandAdd)
except FileNotFoundError:
    print('Commands file not found. Please create a file called \'commands.txt\' in the same directory as this script and run again.')
    quit()

print('-' * 10)
print('This script will connect to the aforementioned hosts and run the commands specified in commands.txt,')
print('then append the results of the commands to \'checksHH-MM-SS.txt\' in the same directory as this script.')
print('If you have any doubts about the commands you\'ve chosen to execute, don\'t do it.')

proceed = input('Proceed? [enter \'y\' for yes, CTRL + C to quit]: ')

if proceed != 'y':
    quit()

for device in switches:
    print(f'Connecting to {device.get("ip")}...')
    run_cmd_print(device, cmds)

if skipped:
    with open(f'checks{scriptTime}.txt', 'a') as outputText:
        outputText.write('/' * 50 + '\n')
        outputText.write('The following hosts were skipped:\n')
    
    print('The following hosts were skipped:')
    
    for item in skipped:
        print(item)
        
        with open(f'checks{scriptTime}.txt', 'a') as outputText:
            outputText.write(f'Connection to {item} failed; no checks performed\n')
    
    print('The hosts above were skipped.')
