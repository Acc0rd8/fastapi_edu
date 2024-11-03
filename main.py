from typing import Annotated
from fastapi import FastAPI, Path

from items_router import router as item_router
from users.user_router import router as user_router

app = FastAPI()


app.include_router(item_router)
app.include_router(user_router)



@app.get('/')
def hello_index():
    return {
        'message': 'Hello index'
    }
    
@app.get('/hello/')
def hello(name: str = 'World'):
    name = name.strip().title()
    return {
        'message': f'Hello {name}'
    }
    
