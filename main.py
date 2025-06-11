from fastapi import FastAPI, Request
import graphene
from graphene import ObjectType, String, Schema

app = FastAPI()

class EchoQuery(ObjectType):
    echo = String(message=String())
    
    def resolve_echo(self, info, message=None):
        return message or "Hello from GraphQL!"

schema = Schema(query=EchoQuery)

@app.get("/api/echo")
async def echo(request: Request):
    return dict(request.query_params)

@app.post("/api/echo")
async def echo_post(request: Request):
    body = await request.json()
    return body

@app.post("/graphql")
async def graphql_endpoint(request: Request):
    body = await request.json()
    query = body.get("query")
    variables = body.get("variables", {})
    result = schema.execute(query, variables=variables)
    
    response = {"data": result.data}
    if result.errors:
        response["errors"] = [str(error) for error in result.errors]
    
    return response

@app.get("/graphql")
async def graphql_get_endpoint(request: Request):
    query = request.query_params.get("query")
    variables_str = request.query_params.get("variables", "{}")
    
    if not query:
        return {"errors": ["Query parameter is required"]}
    
    try:
        import json
        variables = json.loads(variables_str) if variables_str != "{}" else {}
    except json.JSONDecodeError:
        return {"errors": ["Invalid JSON in variables parameter"]}
    
    result = schema.execute(query, variables=variables)
    
    response = {"data": result.data}
    if result.errors:
        response["errors"] = [str(error) for error in result.errors]
    
    return response