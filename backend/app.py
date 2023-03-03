from utils.database_fetches.get_expensive_sensors_and_systems import get_expensive_sensors_and_systems
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers.systems import router as systems_router
from routers.sensors import router as sensors_router

load_dotenv()

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

app.include_router(systems_router, prefix="/systems", tags=["systems"])
app.include_router(sensors_router, prefix="/sensors", tags=["sensors"])


@app.get(
    "/expensive-systems-sensors",
    response_description="Returns the top 3 most expensive systems or sensors. Returned format is a list of tuples, containing the ID along with total cost. E.g. [(1234, 1000.45242), (2791, 923.59532), (3399, 721.80021)]",
)
async def get_expensive_sensors_systems():
    return get_expensive_sensors_and_systems()
