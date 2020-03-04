from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    a: int = None
    b: int = None

@app.post('/test')
def calculate(request_data: Item):
    a = request_data.a
    b = request_data.b
    c = a + b
    res = {"res":c}
    return res

if __name__ == '__main__':
    print("http://127.0.0.1:8080/test")
    import uvicorn
    uvicorn.run(app=app,
                host="127.0.0.1",
                port=8080,
                workers=1)

