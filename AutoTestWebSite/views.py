from django.http import HttpResponse
from django.http import JsonResponse
import json
from common.p2padmin import p2padmin


def home(request):
    return HttpResponse("Hello world ! ")


def msgcode(request):

    if request.method == 'GET':
        try:
             host = request.GET['host']
        except Exception as e:
            print('错误：请求参数不正确')
            return HttpResponse('错误：请求参数不正确')
            # print(e)
        obj_msg = p2padmin(host)  # init
        msg_dic = obj_msg.getmsgcode()
        return HttpResponse(json.dumps(msg_dic, ensure_ascii=False),
                            content_type="application/json,charset=utf-8")  # 防止中午乱码

    if request.method == 'POST':
        host = request.POST.get('host')
        obj_msg = p2padmin(host)#init
        msg_dic = obj_msg.getmsgcode()
        return HttpResponse(json.dumps(msg_dic, ensure_ascii=False),
                            content_type="application/json,charset=utf-8")  # 防止中午乱码



if __name__=='__main__':
    print('abc')