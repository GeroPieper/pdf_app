from fastapi import FastAPI
from app.routes import pdf

app = FastAPI()

# Routen registrieren
app.include_router(pdf.router, prefix="/pdf", tags=["PDFs"])

@app.get("/")
def root():
    return {"message": "PDF App Backend läuft"}
