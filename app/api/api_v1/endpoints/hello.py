from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/hello")
def hello_world():
    return JSONResponse(content="Welcome to my FastApi example")
