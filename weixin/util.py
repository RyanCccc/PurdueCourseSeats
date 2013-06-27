# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

from seats_check.util import *

test_str = "<xml><ToUserName><![CDATA[ryanc]]></ToUserName><FromUserName><![CDATA[shabi]]></FromUserName><CreateTime>1348831860</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[10001]]></Content><MsgId>1234567890123456</MsgId></xml>"

def parse_xml(in_str):
    root = ET.fromstring(in_str) 
    msg = ''
    content =  root.find('Content').text
    tousername = root.find('FromUserName').text
    fromusername = root.find('ToUserName').text
    createtime = root.find('CreateTime').text
    term = ''
    crn = ''
    if len(content) <= 5:
        crn = content.strip()
        term = 'fall2013'
    else:
        crn, term = content.split(' ')
    term_code = convert_term_to_code(term)
    try:
        max_num, curr_num, name, code, number = get_all(crn, term_code)
        rem_num = int(max_num) - int(curr_num)
        msg = '您订阅的课 %s ,课号 %s, Section Number是%s, CRN为%s, 一共有%d个位置, 现在还剩下%d' % (
                name.encode('iso-8859-2'), 
                code.encode('iso-8859-2'),
                number.encode('iso-8859-2'), 
                crn.encode('iso-8859-2'), 
                int(max_num), 
                int(rem_num)
                )
    except:
        msg = "Sorry, the CRN %s is not available for term %s" % (crn, term)
    re_str = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>" % (tousername, fromusername, createtime, msg)
    return re_str
