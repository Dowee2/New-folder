import getpass as login


from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

commands = [
    'int g 1/0/2',
    'description I got here!',
    'shutdown'
]

try:
    device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.25',
    'username': 'cisco',
    'password': 'cisco' #TODO: Change to login.getpass() OR pass in login credentials
    }


    with ConnectHandler(**device) as net_connect:
        device_name = net_connect.find_prompt()[:-1]
        print(device_name)
        net_connect.secret = 'cisco!'
        net_connect.enable()
        net_connect.send_config_set(commands)
        
        filename = f'{device_name}.txt'
        net_connect.save_config
        config = net_connect.send_command('sh run')
        with  open(filename, 'w') as file:
            file.write(config)


except NetMikoTimeoutException:
    print(f"Connection timed out")
except NetMikoAuthenticationException:
    print(f"Authentication failed for")
except Exception as error:
    print(f"Failed to configure: {error}")


#connection = ConnectHandler(**device)






