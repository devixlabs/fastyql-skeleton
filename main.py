from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/api/echo")
async def echo(request: Request):
    return dict(request.query_params)