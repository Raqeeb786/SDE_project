from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models import user
from app.routes.user import router as user_router
from app.routes.auth import router as auth_router
from app.websocket.chat import router as websocket_router
from app.routes.rooms import router as room_router

#Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Backend API",
    description="A robust production-ready FastAPI backend template",
    version="1.0.0",
)

origins = [
    "http://localhost:5173",  # Vite default
    "http://127.0.0.1:5173",
    "https://opulent-space-spork-45rp7rjrpqw274gj-5173.app.github.dev"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(websocket_router)
app.include_router(room_router)

@app.get("/", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "message": "Welcome to the FastAPI Backend Blueprint"
    }
