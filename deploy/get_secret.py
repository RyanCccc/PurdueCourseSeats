def get_password():
    f = open('/srv/project/secret/password','r')
    return f.read()
