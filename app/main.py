from fastapi import FastAPI
from api import router

app = FastAPI()


@app.get('/health')
def health_check():
    return {'status': 'healthy'}


app.include_router(router)
