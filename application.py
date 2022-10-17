"""This module contains the code required to run the backend application."""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from my_math import add, subtract

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    """Root endpoint to check that the application is running."""
    return JSONResponse({"message": "app is running", "success": True}, 200)

@app.get("/add")
def appAdd(a: int, b: int):
    """Endpoint to add two numbers."""
    return JSONResponse({"message": f"{a} + {b} = {add(a,b)}", "success": True}, 200)

@app.get("/subtract")
def appSubtract(a: int, b: int):
    """Endpoint to subtract two numbers."""
    return JSONResponse({"message": f"{a} - {b} = {subtract(a,b)}", "success": True}, 200)

if __name__ == "__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=80, reload=True)
