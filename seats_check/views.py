# Create your views here.
import json
from seats_check.util import get_all

from django.http import HttpResponse

from seats_check.models import Section
from PCS import settings

def seats_check(request, class_crn, term = settings.CURRENT_TERM):
    result = None
    exists = True

    try:
        sec = Section.objects.get(crn = class_crn, term = term) 
    except:
        exists = False

    if not exists: 
        try:
            max_num, curr_num, name, code, number = get_all(class_crn, term)
            result = json.dumps(
                {'code': 1, 
                'content': (max_num, 
                            curr_num, 
                            (max_num - curr_num),
                            name,
                            code,
                            number,
                            )}
            )
        except Exception as e:
            result = json.dumps({'code' : 0, 'content': e.message})
    else:
        result = json.dumps({
            'code': 1,
            'content': (sec.max_seats_num, sec.current_seats_num, sec.remain_seats_num),
            })
    return HttpResponse(result, content_type="application/json")
