def get_password(PRODUCT_MODE):
    path = '/srv/project/secret/password' 
    if not PRODUCT_MODE:
        path = '~/password'
    f = open(path, 'r')
    return f.read().replace('\n','')
