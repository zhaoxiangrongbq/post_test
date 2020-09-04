import requests
import pandas as pd
import random
import json
import datetime
for i in range(1,30000):
    a=i
    b=random.randint(1,100)
    s={"a":a,"b":b}
    t1=datetime.datetime.now()
    result=requests.post(url=r'http://192.168.68.6:8787/post',data=json.dumps(s))
    t2 = datetime.datetime.now()
    result2=json.loads(result.text)
    ms="a :"+str(a)+" b:"+str(b)+" > "+str(result2["msg"])+" time:"+str((t2-t2))
    print(ms)