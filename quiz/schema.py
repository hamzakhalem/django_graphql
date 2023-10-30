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
    all_quiz = DjangoListField(QuizzesType)
    all_quest = DjangoListField(QuestionType)
    all_answers = DjangoListField(AnswerType)

    def resolve_all_quiz(root, info):
        return Quizzes.objects.all()
    
    def resolve_all_quest(root, info):
        return Question.objects.all()


schema = graphene.Schema(query=Query)