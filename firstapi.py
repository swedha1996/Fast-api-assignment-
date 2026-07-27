import fastapi
from fastapi import FastAPI



"""
main.py

A very basic FastAPI web API.

WHAT THIS APP DOES
-------------------
- GET /            -> returns a simple welcome message (JSON)
- GET /greet/{name} -> returns a personalized greeting using a path parameter
- GET /add          -> returns the sum of two numbers passed as query
                       parameters (a, b), to demonstrate query params too

SETUP
-----
    python -m venv venv
    venv\\Scripts\\activate        (Windows)
    source venv/bin/activate      (macOS/Linux)

    pip install fastapi uvicorn

RUN
---
    uvicorn main:app --reload

Then open in your browser:
    http://127.0.0.1:8000/            -> welcome message
    http://127.0.0.1:8000/greet/Swedha -> personalized greeting
    http://127.0.0.1:8000/add?a=2&b=3  -> query-param example
    http://127.0.0.1:8000/docs         -> interactive Swagger UI docs
    http://127.0.0.1:8000/redoc        -> alternative ReDoc docs
"""

from fastapi import FastAPI

app = FastAPI(
    title="My First FastAPI App",
    description="A minimal FastAPI project with a root endpoint and a "
                "couple of parameterized endpoints.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    """Root endpoint - returns a simple welcome message."""
    return {"message": "Welcome to my first FastAPI app!"}


@app.get("/greet/{name}")
def greet(name: str):
    """
    Path parameter example.
    Visiting /greet/Swedha returns a greeting that includes "Swedha".
    """
    return {"message": f"Hello, {name}! Welcome to FastAPI."}


@app.get("/add")
def add_numbers(a: int, b: int):
    """
    Query parameter example.
    Visiting /add?a=2&b=3 returns their sum.
    FastAPI automatically returns a clear validation error in the
    interactive docs if 'a' or 'b' is missing or not a number.
    """
    return {"a": a, "b": b, "sum": a + b}