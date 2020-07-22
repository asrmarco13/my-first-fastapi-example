from fastapi import APIRouter
from api.api_v1.endpoints import hello, item, user


api_router = APIRouter()
api_router.include_router(hello.router, tags=["hello"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(item.router, prefix="/items", tags=["items"])
