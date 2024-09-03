import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
    """
    Hello World
    """
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug",
    )