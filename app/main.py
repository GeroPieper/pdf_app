from fastapi import FastAPI
from app.routes import pdf
from app.database import engine, Base

# Erstellt alle Tabellen, sofern sie noch nicht existieren
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routen registrieren
app.include_router(pdf.router, prefix="/pdf", tags=["PDFs"])

@app.get("/")
def root():
    return {"message": "PDF App Backend läuft"}
