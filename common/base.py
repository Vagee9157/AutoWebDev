import yaml
from common import config
import json

class BaseClass:
    def __init__(self):
        pass

    def readjsonkey(self,key):
        with open(config.JsonFilePath, encoding='utf-8') as f:
             res=json.loads(f.read())
        value=res[key]
        return value

    def writejsonkey(self,key,value):
        res={}
        with open(config.JsonFilePath,mode='r', encoding='utf-8') as f:
             res=json.loads(f.read())

        with open(config.JsonFilePath,mode='w', encoding='utf-8') as f:
            res[key]=value
            res=json.dumps(res)
            f.write(res)

if __name__ == '__main__':

        # yaml_path='D:/New_Auto_2019/Auto_Python/Resource/User/user_info.yaml'
    yaml_path = 'E:/New_Auto_2019/Auto_Python/Resource/User/user_info.yaml'
    abc = BaseClass()
    print(abc.readjsonkey('p2pcookie'))
    abc.writejsonkey('host','http://172.30.2.77:9080')
