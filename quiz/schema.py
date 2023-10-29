import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import *

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id', 'title', 'category', 'quiz')

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'quiz')
class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('question', 'answer_text')

class Query(graphene.ObjectType):


schema = graphene.Schema(query=Query)