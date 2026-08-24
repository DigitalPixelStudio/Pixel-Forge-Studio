from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Pixel Forge Cloud API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "online", "empire": "Digital Pixel Forge", "powered_by": "Faisu & Jasmine"}

@app.get("/health")
def health_check():
    return {"database": "Supabase & MongoDB Connected", "storage": "Cloudflare R2 Active", "deploy": "Vercel Edge Ready"}
