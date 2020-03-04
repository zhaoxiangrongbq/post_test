from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen
import json
import traceback
 
def add(a,b):
    c = int(a) + int(b)
    return str(c)
 
 
class MainHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(32)
    @tornado.gen.coroutine
    def get(self):
        '''get接口'''
        htmlStr = '''
                    <!DOCTYPE HTML><html>
                    <meta charset="utf-8">
                    <head><title>Get page</title></head>
                    <body>
                    <form		action="/post"	method="post" >
                    a:<br>
                    <input type="text"      name ="a"     /><br>
                    b:<br>
                    <input type="text"      name ="b"     /><br>
                    
                    <input type="submit"	value="add"	/>
                    </form></body> </html>
                '''
        self.write(htmlStr)
 
    # @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        '''post接口， 获取参数'''
        a = self.get_argument("a", None)
        b = self.get_argument("b", None)
        yield self.coreOperation(a, b)
 
    @run_on_executor
    def coreOperation(self, a, b):
        '''主函数'''
        try:
            if  a != '' and b != '':
                result = add(a, b)  #可调用其他接口
                if result:
                    result = json.dumps({'code': 200, 'result': result, })
                else:
                    result = json.dumps({'code': 210, 'result': 'no result',})
 
            else:
                result = json.dumps({'code': 211, 'result': 'wrong input a or b', })
            self.write(result)
        except Exception:
            print ('traceback.format_exc():\n%s' % traceback.format_exc())
            result = json.dumps({'code': 503,'result': str(a)+'+'+str(b)})
            self.write(result)
 
if __name__ == "__main__":

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/post', MainHandler)], autoreload=False, debug=False)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8832)
    tornado.ioloop.IOLoop.instance().start()

