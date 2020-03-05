def strip_uuid(uuid):
    return uuid.replace("-", "")

def check_success(resp):
    if "success" in resp:
        return resp['success']
    return False
