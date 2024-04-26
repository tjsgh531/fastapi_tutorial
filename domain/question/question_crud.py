from models import Question
from sqlalchemy.orm import Session
from typing import List

# 테이블 생성하기
def create_question(db: Session, questions: List[Question]):
    for question in questions:
        add_data(db, question)

    
# 모든 데이터 가져오기
def get_question_list(db: Session):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list

# 데이터 하나 가져오기
def get_question(db: Session, id:int):
    _question = db.query(Question).filter(Question.id == id).first()
    return _question

# 데이터 추가하기
def add_data(db: Session, question: Question):
    db.add(question)
    db.commit()
    db.refresh(question)

# 데이터 삭제하기
def delete_data(db: Session, id:int):
    db.query(Question).filter(Question.id == id).delete()
    db.commit()

# 데이터 수정하기
def update_data(db: Session, id:int, question: Question):
    db.query(Question).filter(Question.id == id).update(question)
    db.commit()
    

