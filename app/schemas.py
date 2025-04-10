from pydantic import BaseModel
from datetime import datetime


class PDFBase(BaseModel):
    filename: str
    unique_filename: str


class PDFCreate(PDFBase):
    pass


class PDF(PDFBase):
    id: int
    upload_date: datetime

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
