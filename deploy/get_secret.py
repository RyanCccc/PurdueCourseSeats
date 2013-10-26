from os import path

PCS_DIR = path.abspath(path.dirname(__file__))
PROJECT_DIR = path.abspath(path.join(PCS_DIR, '..'))

def get_password():
    pass_path = path.join(PROJECT_DIR,'password')
    f = open(pass_path, 'r')
    return f.read().replace('\n','')
