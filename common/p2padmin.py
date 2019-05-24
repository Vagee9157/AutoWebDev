import requests
from common.base import BaseClass
import re
class p2padmin:
    base=BaseClass()

    def __init__(self,host,user='admin',password='password'):
        self.host=host
        self.user=user
        self.password=password
        self.header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        self.header['Cookie']=self.base.readjsonkey('p2pcookie')
        #判断cookie是否有效，登录
        self.is_login()

    def is_login(self):
        index_url=self.host+'/index.action'
        res=requests.get(index_url,headers=self.header)
        title=re.findall(r'<title>(.*?)</title>',res.text,re.S)[0]
        try:
            if title=='网站管理员登录':
                self.login()
            elif title=='管理中心':
                print('登录成功！')
            else:
                raise Exception("登录发生错误")
        except Exception as e:
            print(e)


    def login(self):
        url=self.host+'/admin/index.action'
        data={'username':self.user,'password':self.password}
        res=requests.post(url,data=data,headers=self.header)
        try:
            assert res.text=='true'
            self.base.writejsonkey('p2pcookie', res.headers['Set-Cookie'])
        except Exception as e:
            print(e)


    def getmsgcode(self):
        url=self.host+'/smsQueryAction.action'
        msg_dic = {'host': self.host,}
        msg_list=[]
        res=requests.get(url,headers=self.header)
        msg=re.findall(r'<tr\s.*?</tr>',res.text,re.S)[1:10]#取10条，0为标题
        for item in msg:
            item_dic = {}
            td=re.findall(r'<td align="center">(.*?)</td>',item,re.S)
            phone=td[0]
            code=td[1]
            item_dic['code'] = code
            item_dic['phone']=phone
            msg_list.append(item_dic)
        # msg_dic={'host':self.host,'msg':[{'phone':18926039157,'msgcode':123456}]}
        msg_dic['msg']=msg_list
        return msg_dic


if __name__=='__main__':
    obj=p2padmin('http://172.30.2.77:9080')
    print(obj.getmsgcode())
    # obj.login()
    # obj.is_login()