import json


def load_upload_packets_from_file(filename):
    content = open(filename, 'r').read()
    content = content.replace('][', '],[')
    content = "[%s]" % content
    saved_data = json.loads(content)
    packets = [json.loads(d) for pkt_list in saved_data for d in pkt_list]
    return packets


upload_data = load_upload_packets_from_file(
    filename='/Users/msachdev/tmp/scrybe/upload_data/perf_test_titanic_2019-11-25_17-16-02.log')

upload_data = load_upload_packets_from_file(
    filename='/Users/msachdev/tmp/scrybe/upload_data/interactive_2019-11-25_17-46-53.log')

print('\n'.join([(json.dumps(d, indent=2)) for d in upload_data if d['data_type'] == 'dataset']))

len(upload_data)