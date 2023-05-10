from django.urls import path
from . import views

urlpatterns = [
    path('tag/list-create/', views.TagListCreate.as_view()),
    path('category/list-create/', views.CategoryListCreate.as_view()),
    path('contact/list-create/', views.ContactListCreate.as_view()),
    path('subscribe/list-create/', views.SubscribeListCreate.as_view()),
    path('f-a-q/list-create/', views.FAQListCreate.as_view()),
    path('faq/<int:question_id>/answer-list-create/', views.AnswerListCreate.as_view()),
]
