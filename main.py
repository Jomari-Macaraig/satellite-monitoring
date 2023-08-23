from fastapi import FastAPI

app = FastAPI()


@app.get("/stats")
async def get_satellite_statistics():
    return {
        "minimum": "",
        "maximum": "",
        "average": "",
    }


@app.get("/health")
async def get_satellite_health():
    return {
        "Message": "Health"
    }