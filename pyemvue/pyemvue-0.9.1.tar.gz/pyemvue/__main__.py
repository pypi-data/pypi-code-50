import pyemvue

def main():
    data = {}
    email = None
    passw = None
    idToken = None
    accessToken = None
    refreshToken = None
    try:
        with open('keys.json') as f:
            data = json.load(f)
    except:
        print('Please create a "keys.json" file containing the "email" and "password"')
        sys.exit(1)
    if ('email' not in data or 'password' not in data) and ('idToken' not in data or 'accessToken' not in data or 'refreshToken' not in data):
        print('Please create a "keys.json" file containing the "email" and "password"')
        sys.exit(1)
    canLogIn = False
    if 'email' in data:
        email = data['email']
        if 'password' in data:
            passw = data['password']
            canLogIn = True
    if 'idToken' in data and 'accessToken' in data and 'refreshToken' in data:
        idToken = data['idToken']
        accessToken = data['accessToken']
        refreshToken = data['refreshToken']
        canLogIn = True
    if not canLogIn:
        print('Please create a "keys.json" file containing the "email" and "password"')
        sys.exit(1)
    vue = PyEmVue()
    vue.login(email, passw, idToken, accessToken, refreshToken, token_storage_file='keys.json')
    print('Logged in. Authtoken follows:')
    print(vue.cognito.id_token)
    print()
    devices = vue.get_devices()
    for device in devices:
        print(device.device_gid, device.manufacturer_id, device.model, device.firmware)
        for chan in device.channels:
            print('\t', chan.device_gid, chan.name, chan.channel_num, chan.channel_multiplier)
    print(vue.get_total_usage(devices[0].channels[0], TotalTimeFrame.MONTH.value) / 1000, 'kwh used month to date')
    print(vue.get_total_usage(devices[0].channels[0], TotalTimeFrame.ALL.value) / 1000, 'kwh used total')
    now = datetime.datetime.utcnow()
    minAgo = now - datetime.timedelta(minutes=1)
    print('Total usage over the last day in kwh: ')
    use = vue.get_recent_usage(Scale.DAY.value)
    for chan in use:
        print(f'{chan.device_gid} ({chan.channel_num}): {chan.usage/1000} kwh')
    print('Average usage over the last minute in watts: ')
    use = vue.get_recent_usage(Scale.MINUTE.value)
    for chan in use:
        print(f'{chan.device_gid} ({chan.channel_num}): {chan.usage} W')
    
    print('Usage over the last minute in watts: ', vue.get_usage_over_time(devices[0].channels[0], minAgo, now))
    

if __name__ == '__main__':
    main()