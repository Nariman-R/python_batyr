from fastapi import FastAPI


app = FastAPI()


@app.get('/health')
def health()-> dict:
    return {'status': 'ok'}

@app.post("/ping_test")
def ping(param1: str):
    print(param1)
    if param1=="ping":
      return {"pong"}
    else:
        return {"wrong parameter"}