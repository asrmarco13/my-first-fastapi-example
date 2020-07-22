import uvicorn
from fastapi import FastAPI
from api.api_v1.apis import api_router
from core.database import engine
from core.settings import settings
from models import item, user

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)

if __name__ == "__main__":
    item.Base.metadata.create_all(bind=engine)
    user.Base.metadata.create_all(bind=engine)
    uvicorn.run("app:app", port=8080, log_level="debug")
