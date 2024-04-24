from fastapi import APIRouter

from database import SessionLocal
from models import Question

router = APIRouter(
    prefix="/question",
)

@router.get("/")
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.createdate.desc()).all()
    db.close()

    return _question_list