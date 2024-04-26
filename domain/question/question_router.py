from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database import get_db
from domain.question import question_schema, question_crud

from fastapi.templating import Jinja2Templates



router = APIRouter(
    prefix="/question",
)

templates = Jinja2Templates(directory="templates")

@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):

    _question_list = question_crud.get_question_list(db)
    return _question_list

@router.get('/')
def home(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get('/show_list')
def show_list(request : Request):
    return templates.TemplateResponse("show_list.html", {"request": request})
