from cautil import get_resource

def ss():
    resource = get_resource('Email')
    print('df')
    print(resource.send())
