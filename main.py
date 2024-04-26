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
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=False)