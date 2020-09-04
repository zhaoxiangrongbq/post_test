import numpy as np
import pandas as pd
import json
from flask import Flask,request,jsonify
app=Flask(__name__)

def get_re(a,b):
    c=a+b
    return c
@app.route('/model',methods=['post'],strict_slashes=False)
def nt():
    pa=request.json
    print(pa)
    a=pa['a']
    b=pa['b']
    c=get_re(a,b)
    resu={"code":0,"result":c}
    return jsonify(resu)
if __name__ == '__main__':
    app.config['JSON_AS_ASCII']=False
    app.run(host='127.0.0.1',port=8888,threaded=True)
# 调用
# json.loads(requests.post(url=r'http://127.0.0.1:8888/model',json={"a":3,"b":5}).text)