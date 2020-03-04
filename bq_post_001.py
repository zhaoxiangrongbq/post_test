import tornado.ioloop
from concurrent.futures import ThreadPoolExecutor
from tornado.httpserver import  HTTPServer
import json
from tornado.web import Application,RequestHandler,url
from tornado.escape import json_decode,json_encode
def sumsum(a,b):
    c=a+b
    return  c

class MainHandler(RequestHandler):
    executor = ThreadPoolExecutor(32)
    def get(self):
        try:
            a=self.get_argument("a",None)
            b = self.get_argument("b", None)
            print(a,b)
            result = json.dumps({"code": 200, "msg": str(int(a) + int(b))})
            print(result)
            self.write(result)
        except Exception as e:
            self.write(json_encode({"code":400,"msg":"朕没有写get方法哦，试试post吧 \n there is no get ,try use post","error":str(e)}))

    def post(self):
        try:
            a = json.loads(self.request.body)["a"]
            b = json.loads(self.request.body)["b"]
            print("a ",a,"b ",b)
            result=json.dumps({"code":200,"msg":str(a+b)})
            self.write(result)
        except Exception as e:
            result={"code":404,"msg":"混蛋！你输入了啥玩意，出错了啊","error":self.request.body,"er":str(e)}
            self.write(result)
if __name__ == '__main__':
    app=Application(handlers=[(r'/post',MainHandler)],autoreload=False,debug=False)
    httpserver=HTTPServer(app)
    httpserver.listen(8787)
    tornado.ioloop.IOLoop.instance().start()