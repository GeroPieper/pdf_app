from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Query
import shutil, os, uuid
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload", response_model=schemas.PDF)
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(database.get_db)):
    # Generiere einen eindeutigen Dateinamen basierend auf einer UUID
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_location = os.path.join(UPLOAD_DIR, unique_filename)

    # Speichere die Datei
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # PDF-Datensatz in DB anlegen
    pdf_in = schemas.PDFCreate(filename=file.filename, unique_filename=unique_filename)
    db_pdf = crud.create_pdf(db, pdf_in)
    return db_pdf


@router.get("/", response_model=list[schemas.PDF])
def list_pdfs(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """
    Zeigt alle in der Datenbank gespeicherten PDFs an.
    """
    pdfs = crud.get_pdfs(db, skip=skip, limit=limit)
    return pdfs


@router.get("/id/{pdf_id}", response_model=schemas.PDF)
def read_pdf_by_id(pdf_id: int, db: Session = Depends(database.get_db)):
    """
    Zeigt Details einer PDF anhand ihrer ID an.
    """
    pdf = crud.get_pdf(db, pdf_id=pdf_id)
    if not pdf:
        raise HTTPException(status_code=404, detail="PDF nicht gefunden")
    return pdf


@router.get("/search", response_model=list[schemas.PDF])
def search_pdfs(query: str = Query(..., description="Suchbegriff für Dateinamen"),
                skip: int = 0, limit: int = 100,
                db: Session = Depends(database.get_db)):
    """
    Sucht PDFs anhand eines Suchbegriffs im Dateinamen.
    """
    pdfs = crud.search_pdfs(db, query, skip=skip, limit=limit)
    return pdfs

