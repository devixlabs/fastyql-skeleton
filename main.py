from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/api/echo")
async def echo(request: Request):
    return dict(request.query_params)

@app.post("/api/echo")
async def echo_post(request: Request):
    body = await request.json()
    return body