from rest_framework import generics, permissions
from ..models import Category, Tag, Contact, Subscribe, FAQ, Answer
from .serializers import TagSerializer, CategorySerializer, ContactSerializer, SubscribeSerializer, FAQGETSerializer, FAQPOSTSerializer, \
    AnswerPOSTSerializer, AnswerGETSerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]


class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]


class SubscribeListCreate(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [permissions.AllowAny]
    

class FAQListCreate(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQGETSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FAQPOSTSerializer
        return super().get_serializer_class()


class AnswerListCreate(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerGETSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AnswerPOSTSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        qs = super().get_queryset()
        question_id = self.kwargs.get('question_id')
        qs = qs.filter(question_id=question_id)
        return qs

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['question_id'] = self.kwargs.get('question_id')
        return ctx
