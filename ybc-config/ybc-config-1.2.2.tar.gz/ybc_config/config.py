import os
profiles_config = {
    'online': {
        'prefix': 'https://www.yuanfudao.com',
        'prefix-oss': 'https://www.yuanfudao.com/oss/ybc-online',
        'websocket': 'ws://ke.yuanfudao.ws/tutor-ybc-sandbox-agent-server/api/ws',
        'course-api-prefix': 'https://www.yuanfudao.com/tutor-ybc-course-api-v3/api',
        'test-file-prefix': 'https://ke.yuanfudao.ws/oss/ybc-test/test-files',
        'resource-file-prefix':
            'https://www.yuanfudao.com/oss/ybc-online/ybc_courseapi/resource',
    },
    'test': {
        'prefix': 'https://ke.yuanfudao.ws',
        'prefix-oss': 'https://ke.yuanfudao.ws/oss/ybc-test',
        'websocket': 'ws://ke.yuanfudao.ws/tutor-ybc-sandbox-agent-server/api/ws',
        'course-api-prefix': 'https://ke.yuanfudao.ws/tutor-ybc-course-api-v3/api',
        'test-file-prefix': 'https://ke.yuanfudao.ws/oss/ybc-test/test-files',
        'resource-file-prefix':
            'https://ke.yuanfudao.ws/oss/ybc-test/ybc_courseapi/resource',
    },
    'local': {
        'prefix': 'http://local.yuanfudao.ws:8080',
        'prefix-oss': 'https://ke.yuanfudao.ws/oss/ybc-test',
        'websocket': 'ws://local.yuanfudao.ws:8080/tutor-ybc-sandbox-agent-server/api/ws',
        'course-api-prefix': 'http://local.yuanfudao.ws:8080/tutor-ybc-course-api-v3/api',
        'test-file-prefix': 'https://ke.yuanfudao.ws/oss/ybc-test/test-files',
        'resource-file-prefix':
            'https://ke.yuanfudao.ws/oss/ybc-test/ybc_courseapi/resource',
    }
}
uri = '/tutor-ybc-course-api-v2/api'


def _read_config(key):
    return os.environ[key] if key in os.environ else None


config = {}
ybc_profile = _read_config('YBC_PROFILE')
if ybc_profile is not None and ybc_profile in profiles_config:
    config = profiles_config[ybc_profile]
else:
    config = profiles_config['online']
