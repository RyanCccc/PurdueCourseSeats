# Create your views here.
import json
from seats_check.util import get_all

from django.views.decorators.csrf import csrf_exempt 
from django.http import HttpResponse

from seats_check.models import Section
from PCS import settings

@csrf_exempt
def seats_check(request, class_crn = None):
    result = None
    exists = True

    #GET
    if request.method == 'GET':
        term = request.GET.get('term') or settings.CURRENT_TERM
        try:
            sec = Section.objects.get(crn = class_crn, term = term) 
        except:
            exists = False

        exists = True
        
        if not exists: 
            try:
                max_num, curr_num, name, code, number = get_all(class_crn, term)
                result = json.dumps(
                    {'code': 1, 
                        'content': {'max_num' : max_num, 
                                    'curr_num' : curr_num, 
                                    'rem_num' : (max_num - curr_num),
                                    'name' : name,
                                    'code' : code,
                                    'number' : number,
                                   }
                    }
                )
            except Exception as e:
                result = json.dumps({'code' : 0, 'content': e.message})
        else:
            max_num = sec.max_seats_num
            curr_num = sec.current_seats_num
            rem_num = sec.remain_seats_num
            name = sec.name
            code = sec.code
            number = sec.number
            result = json.dumps(
                {'code': 1, 
                    'content': {'max_num' : max_num, 
                                'curr_num' : curr_num, 
                                'rem_num' : rem_num,
                                'name' : name,
                                'code' : code,
                                'number' : number,
                               }
                }
            )

    # POST
    elif request.method == 'POST':
        post_json = json.loads(request.body)
        term = post_json.get('term')
        if not term:
            term = settings.CURRENT_TERM
        crns = post_json.get('content')
        result = []
        for crn in crns:
            try:
                max_num, curr_num, name, code, number = get_all(crn, term)
                result += json.dumps(
                    {'code': 1, 
                        'content': {'max_num' : max_num, 
                                    'curr_num' : curr_num, 
                                    'rem_num' : (max_num - curr_num),
                                    'name' : name,
                                    'code' : code,
                                    'number' : number,
                                   }
                    }
                )
            except Exception as e:
                result = json.dumps({'code' : 0, 'content': e.message})

    return HttpResponse(result, content_type="application/json")
