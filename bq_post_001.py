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
    #executor = ThreadPoolExecutor(32)
    def initialize(self,poo):
        self.p=poo

    def get(self):
        try:
            a=self.get_argument("a",None)
            b = self.get_argument("b", None)
            print(a,b)
            result = json.dumps({"code": 200, "msg": str(int(a) + int(b)+int(self.p))})
            print(result)
            self.write(result)
        except Exception as e:

            self.write(json_encode({"code":400,"msg":"朕没有写get方法哦，试试post吧 \n there is no get ,try use post","error":str(e)}))

    def post(self):


        try:
            a = json.loads(self.request.body)["a"]
            b = json.loads(self.request.body)["b"]
            c=sumsum(a,b)
            c=sumsum(c,self.p)
            print("a ",a,"b ",b)
            result=json.dumps({"code":200,"msg":str(c)})
            self.write(result)
        except Exception as e:
            result={"code":404
                ,"msg":"混蛋！你输入了啥玩意，出错了啊","error":self.request.body,"er":str(e)}
            self.write(result)

if __name__ == '__main__':
    p=1000
    # app=Application(handlers=[(r'/post',MainHandler)],autoreload=False,debug=False)
    app=Application(handlers=[url(r'/post',MainHandler,dict(poo=p))],autoreload=False,debug=False)
###单线程
    httpserver=HTTPServer(app)
    httpserver.listen(8787)

####多线程

    # sockets = tornado.netutil.bind_sockets(8787)
    # tornado.process.fork_processes(3)
    # httpserver=HTTPServer(app)
    # httpserver.add_sockets(sockets)

    # tornado.ioloop.IOLoop.instance().start()
    tornado.ioloop.IOLoop.current().start()