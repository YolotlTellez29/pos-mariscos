from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import auth, pedidos

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O restringe a ["http://localhost:5500"] si usas Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(pedidos.router)
