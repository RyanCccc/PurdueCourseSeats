import Cookie
import hashlib
import json
import httplib, urllib

from weixin.models import Auth

ACCOUNT = 'chenrd769@gmail.com'
PASSWORD = 'csgtc0433'
HOST = 'mp.weixin.qq.com'
LOGIN_PATH = '/cgi-bin/login?lang=zh_CN'
SENDMSG_PATH = '/cgi-bin/singlesend?t=ajax-response&lang=zh_CN'
REFERER_URL = 'https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&lang=zh_CN'

PARAMS = {
    'type' : 1,
    'content' : '',
    'error' : 'false',
    'tofakeid' : None,
    'token' : None,
    'ajax' : 1,
}
HEADERS = {
    'Referer' : REFERER_URL, 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'mp.weixin.qq.com',
    'Content-Length' : 72,
    'Connection': 'Keep-Alive',
    'Cache-Control': 'no-cache',
    'Cookie' : '',
}

def sendMsg(msg, userid):
    # Get cookie and token
    auth = Auth.objects.all()[0]
    cookie = auth.cookie
    cookie = cookie + "; RK=HAgLZ+xrcE; pgv_pvid=7299549813; o_cookie=799080508"
    token = auth.token

    HEADERS['Cookie'] = cookie
    PARAMS['token'] = token
    PARAMS['tofakeid'] = userid
    PARAMS['content'] = msg
    conn = httplib.HTTPSConnection("mp.weixin.qq.com")
    print urllib.urlencode(PARAMS)
    print HEADERS['Cookie']
    conn.request("POST", SENDMSG_PATH, 
        urllib.urlencode(PARAMS), HEADERS)
    response = conn.getresponse()
    data = response.read()
    if not 'ok' in data:
        print 'Error %s' % data
        return False
    else:
        print 'Send message successfully!!'
        return True

def login():
    token = ''
    pwd = hashlib.md5(PASSWORD).hexdigest()
    params = {
        'username' : ACCOUNT,
        'pwd' : pwd,
        'imgcode' : '',
        'f' : 'json',
    }
    connect = httplib.HTTPSConnection(HOST)
    connect.request('POST', LOGIN_PATH, urllib.urlencode(params))
    resp = connect.getresponse()
    body = resp.read()
    body = json.loads(body)
    if body.get('ErrCode'):
        print 'Error when log in'
        return False
    else:
        back_url = body.get('ErrMsg')
        token = back_url[(back_url.index('token=')+len('token=')):]
    headers = resp.getheaders()
    raw_cookie = [obj for obj in headers if 'set-cookie' in obj][0][1] 
    cookie = Cookie.SimpleCookie()
    cookie.load(raw_cookie)
    str_cookie = ''
    for k, v in cookie.iteritems():
        str_cookie += k + ':' + v.value + '; '
    str_cookie = str_cookie[:-2]
    auth = None
    auths = Auth.objects.all()
    if auths:
        auth = auths[0]
        auth.token = token
        auth.cookie = str_cookie
    else:
        auth = Auth(token = token, cookie = str_cookie)
    auth.save()
    return True
