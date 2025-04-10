from sqlalchemy.orm import Session
from app import models, schemas


def create_pdf(db: Session, pdf: schemas.PDFCreate):
    db_pdf = models.PDF(filename=pdf.filename, unique_filename=pdf.unique_filename)
    db.add(db_pdf)
    db.commit()
    db.refresh(db_pdf)
    return db_pdf


def get_pdf(db: Session, pdf_id: int = None, pdf_unique_name: str = None):
    if pdf_id is not None:
        return db.query(models.PDF).filter(models.PDF.id == pdf_id).first()
    elif pdf_unique_name is not None:
        return db.query(models.PDF).filter(models.PDF.unique_filename == pdf_unique_name).first()
    else:
        raise ValueError("Bitte entweder 'pdf_id' oder 'pdf_unique_name' angeben.")


def get_pdfs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PDF).offset(skip).limit(limit).all()


def search_pdfs(db: Session, query: str, skip: int = 0, limit: int = 100):
    # Mit 'ilike' wird eine case-insensitive Suche durchgeführt
    return (
        db.query(models.PDF)
        .filter(models.PDF.filename.ilike(f"%{query}%"))
        .offset(skip)
        .limit(limit)
        .all())

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()
