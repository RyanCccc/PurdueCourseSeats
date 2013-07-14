import hashlib

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 

from weixin.util import parse_xml
# Create your views here.

TOKEN = 'ryancccc'


@csrf_exempt
def index(request):
    if request.method == 'GET':
        echostr = request.GET.get('echostr')
        if _checkSig(request.GET):
            return HttpResponse(echostr, content_type = 'text/plain')
        else:
            return HttpResponse('error', content_type = 'text/plain')
    elif request.method == 'POST':
        resp = parse_xml(request.body)
        return HttpResponse(resp)

def _checkSig(param):
    sig = param.get('signature')
    timestamp = param.get('timestamp')
    nonce = param.get('nonce')

    array = [TOKEN, timestamp, nonce]
    array.sort()
    v = ''.join(array)
    sha = hashlib.sha1(v)
    if sha.hexdigest() == sig:
        return True
    else:
        return False
