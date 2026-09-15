"""Starter application for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI


app = FastAPI(title="Task API")


@app.get("/health")
def health_check():
    """Return the API health status."""
    return {"status": "ok"}


# Add the task model, in-memory storage, and task routes below.
# Run with: uvicorn starter-code:app --reload