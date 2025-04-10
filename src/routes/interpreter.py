from fastapi import FastAPI, HTTPException, Request ,APIRouter
from tools.run_container import run_code_in_container
import json

interpreter = APIRouter(
    prefix = "/api/interpreter",
    tags = ["api"],
)

@interpreter.post("/execute")
async def execute_code(request: Request):
    """
    API endpoint to execute Python code in a Docker container.
    
    Expected JSON format:
    {
        "code": "print('Hello, World!')"
    }
    """
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Request must be JSON")
    
    if "code" not in data:
        raise HTTPException(status_code=400, detail="Missing 'code' field")
    
    python_code = data["code"]
    python_code_stripped = python_code.strip('"""')
    
    output, errors = await run_code_in_container(python_code_stripped)
    
    return {
        "output": output,
        "errors": errors
    }


@interpreter.get("/health")
async def health_check():
    """Simple health check endpoint"""
    return {"status": "running"}
