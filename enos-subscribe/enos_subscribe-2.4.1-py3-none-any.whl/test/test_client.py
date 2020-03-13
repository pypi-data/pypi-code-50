from enos_subscribe import DataClient

if __name__ == '__main__':
    client = DataClient(host='subscribe-ppe1.envisioniot.com', port='9001',
                        access_key='b1b08b88-6dd5-4470-aa40-b27af446c1e9',
                        access_secret='ef9e10f0-4ff4-4429-90c5-21aab307062f')

    client.subscribe(sub_id='test_dingyue2')

    for message in client:
        print(message)