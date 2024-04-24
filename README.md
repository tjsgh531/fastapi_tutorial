# FastAPI tutorial

## File structure

|_ main.py

|_ database.py

|_ models.py

|_ domain

|    |_ answer

|    |_ user

|    |_question

|        |_question_router.py

|        |_question_crud.py

|        |_question_schema.py

|_ frontend

    |_ index.html

    |_ src

        |_js

        |_css

## library

```shell
pip install fastapi

pip install uvicorn

pip install sqlalchemy

pip install psycopg2

pip install alembic
```

## Models

Question Models

|feature|description|
|:----:|:------------|
|id| INT : id of question data|
|subject| STR : title of question|
|content| STR : content of question|
|create_date| DATEFRAME : created date|

Answer Models

|feature|description|
|:----:|:------------|
|id| INT : id of answer data|
|question_id| INT : id of question related answer data|
|content| STR : content of answer|
|create_date| DATEFRAME : create date|


