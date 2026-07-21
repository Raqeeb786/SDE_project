from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Example imports for external route modules (uncomment as you build them)
# from app.routers import auth_router, users_router, items_router

# 1. Initialize the FastAPI instance
app = FastAPI(
    title="My Backend API",
    description="A robust production-ready FastAPI backend template",
    version="1.0.0"
)

# 2. Configure CORS Middleware (Crucial for frontend connection)
ORIGINS = [
    "http://localhost:3000",      # React local development
    "http://127.0.0.1:3000",
    "https://yourproductiondomain.com" # Production client
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],          # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allows all headers
)

# 3. Include Routers (Modular Endpoints)
# app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])
# app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])

# 4. Root Health Check Endpoint
@app.get("/", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "message": "Welcome to the FastAPI Backend Blueprint"
    }


