from fastapi import APIRouter
from utils.database_fetches.get_systems import get_all_systems
from utils.database_fetches.get_sensors_in_system import get_sensors_in_system

router = APIRouter()


@router.get("/", response_description="Get list of all systems")
async def get_systems():
    return get_all_systems()


@router.get("/{systemid}/sensors", response_description="Get list of all sensors in a system")
async def get_sensors(systemid):
    return get_sensors_in_system(systemid)
