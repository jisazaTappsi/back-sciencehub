from fastapi import FastAPI
from api.urls import router

app = FastAPI(title="ScienceHub API",
              description="Insatiable thirst for discovery", version="1.0.0", )

origins = [
    "http://sciencehub.com",
]


app.include_router(router)
