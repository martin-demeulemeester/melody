"""
Entry point for running the FastAPI application.
Run this file with: python run.py
Or use uvicorn directly: uvicorn app.main:app --reload
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

