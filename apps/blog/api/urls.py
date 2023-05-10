from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('post-rud/<int:pk>/', views.BodyRUD.as_view()),
    path('<int:post_id>/comment-list-create/', views.CommentListCreate.as_view()),

]
