import json

FILE_NAME = 'user.json'

def read_user_info():
    with open(FILE_NAME) as json_file:
        json_data = json.load(json_file)
        return json_data

def write_user_info(data):
    with open(FILE_NAME, "w") as json_file: 
        json_file.write(data) 

# --------------------------------------------------

def get_blog_name():
    return read_user_info()['blog_name']

def get_client_id():
    return read_user_info()['client_id']

def get_client_secret():
    return read_user_info()['client_secret']

def get_access_token():
    return read_user_info()['access_token']

def get_categories():
    return read_user_info()['categories'] or []

def get_category_id_by_name(name):
    for c in get_categories():
        if c['name'] == name:
            return c['id']
    
    raise Exception('고딴거 없습니다')

# --------------------------------------------------

def write_access_token(token):
    data = read_user_info()
    data['access_token'] = token
    write_user_info(json.dumps(data, indent = 4))

def write_categories(categories):
    data = read_user_info()
    data['categories'] = categories
    write_user_info(json.dumps(data, indent = 4))