import subprocess
import csv
import os
from wifi import Cell, Scheme

def search_wifi():
    wifi_list = {}
    cells = Cell.all('wlan0')
    for connection in cells:
        SSID = connection.ssid
        enc = connection.encrypted
        if SSID:
            wifi_list[SSID] = enc

    return wifi_list




def write_previous_connections(SSID):
    ssids = read_json('previous')
    if SSID not in ssids:

        ssids.append(SSID)
    
    write_json('previous', ssids)


def search_connected():
    process = subprocess.Popen(['nmcli', 'd'], stdout=subprocess.PIPE)
    #process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()
    #print(stdout.decode('utf-8').splitlines())
    reader = csv.DictReader(stdout.decode('utf-8').splitlines(),
                            delimiter=' ', skipinitialspace=True,
                            fieldnames=['NAME', 'UUID',
                                        'TYPE', 'DEVICE',])

    wifi_list = {}
    connected = {'connection' : False}
    for row in reader:
        if row ['TYPE'] == 'wifi':
            uuid = row['UUID']
            name = row['NAME']
            wifi_list[name] = connection
    return connected, wifi_list


#  nmcli d up <name>
def disconnect(wifi_name):
    os.system(f'nmcli con down id {wifi_name}')

def request_password():
    # send a socket requesting a password
    return False

def connect_wifi(name, password=None):

    previous =  read_json('previous')
    print(previous, "previous")
   
    if name in previous:
         os.system(f'nmcli c up {name}')
    else:
        os.system(f'nmcli device wifi connect {name} password {password}')

    # if password == None:
    
    #     process = subprocess.Popen(['nmcli', 'c', 'up', name], stdout=subprocess.PIPE)
        
    #     stdout, stderr = process.communicate()
    #     read = stdout.decode('utf-8')
    #     print(read)
    #     if len(read) == 0:
    #         return request_password()
    #     return True
    # 
def search():
    pass

def read_network_list():
    pass
def save_network_list():
    pass
def read_network():
    #nmcli d
    pass
def ask_password():
    #socket promt for password
    pass

if __name__ == '__main__':
    wifi_list = search_wifi()
    print(wifi_list)
    # if connection['connection'] == False:
    #     wifi = next(iter(wifi_list))
    #     print(wifi, "no connect")
    #     val = connect(str(wifi))
    #     if val == False:
    #         connect(str(wifi), 'orangejet')
    # else:
    #     wifi = next(iter(wifi_list))
    #     print("connedcted")
    #     disconnect(wifi)
    # disconnect(connect[True])
