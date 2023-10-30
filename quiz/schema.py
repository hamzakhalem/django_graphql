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
        fields = ('id','question', 'answer_text')

class Query(graphene.ObjectType):
    all_quiz = graphene.Field(QuizzesType, id= graphene.Int())
    all_quest = graphene.Field(QuestionType, id= graphene.Int())
    all_answers = graphene.List(AnswerType, id= graphene.Int())

    def resolve_all_quiz(root, info, id):
        return Quizzes.objects.get(pk=id)
    
    def resolve_all_quest(root, info, id):
        return Question.objects.get(pk=id)
    
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


schema = graphene.Schema(query=Query)