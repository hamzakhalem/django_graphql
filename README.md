# Django GraphQL API

A GraphQL API built with Django and [Graphene](https://docs.graphene-python.org/projects/django/). It has two schemas: a simple books schema and a quiz schema with categories, quizzes, questions and answers.

## Features

- **Books schema:** list all books
- **Quiz schema:** get a quiz by id, a question by id, and the answers of a question
- Quiz models with categories, difficulty levels, an active flag and a correct-answer flag
- GraphiQL in the browser to explore and test queries
- Everything is manageable from the Django admin

## Endpoints

| Path | Schema |
| --- | --- |
| `/garphql` | Books |
| `/garphqlquiz` | Quiz |

Both open GraphiQL in the browser.

## Example queries

```graphql
# /garphql
{
  allBooks {
    id
    title
  }
}
```

```graphql
# /garphqlquiz
{
  allQuiz(id: 1) {
    id
    title
    category { name }
  }
  allAnswers(id: 1) {
    id
    answerText
  }
}
```

## Built with

- Python 3, Django 4.2
- Graphene 3, graphene-django
- SQLite

## Run it locally

```bash
git clone https://github.com/hamzakhalem/django_graphql.git
cd django_graphql
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Add a few books or quizzes in http://127.0.0.1:8000/admin/, then query them at http://127.0.0.1:8000/garphql.

## Project structure

```
core/    Project settings and root URLs
books/   Book model and books schema
quiz/    Category, quiz, question and answer models, and the quiz schema
```
