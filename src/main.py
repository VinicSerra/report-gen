from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse
import uvicorn
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
from src import modules


 
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(modules.reports.router)
 

if __name__ == "__main__":
    uvicorn.run(app, host=str("localhost"), port=int(8001))
    logger.info("API Server iniciado")
   