from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from domain.question import question_router

'''테이블 생성 코드(alembic 없이)
import models
from database import engine
models.Base.metadata.create_all(engine)
'''

app = FastAPI()

app.include_router(question_router.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

upload_dummy_data = False

# Question 더미 데이터 넣기
if (upload_dummy_data ):
    from dummy_data import questions, answers
    from models import Question
    from database import get_db
    from fastapi import Depends
    from domain.question import question_crud

    for question in questions:
        new_question = Question(**question)
        question_crud.add_data(db=Depends(get_db), question=new_question)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=False)