from fastapi import FastAPI
from routes.interpreter import interpreter 
import uvicorn

app = FastAPI()

app.include_router(interpreter)

uvicorn.run(app, host='127.0.0.1', port=5000)