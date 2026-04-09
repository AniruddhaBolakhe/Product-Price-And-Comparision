from fastapi import FastAPI
from routes.auth import auth_router


app=FastAPI(title='Product Price and Comparision')
app.include_router(auth_router , tags=['Authentication'])

@app.get('/')
def home():
    return "Product Price and Comparision Tool"
@app.get('/health')
def health():
    return {"message":"ok"}
