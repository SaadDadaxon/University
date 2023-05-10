from django.urls import path
from . import views

urlpatterns = [
    path('course-list-create/', views.CourseListCreate.as_view()),
    path('<int:pk>/', views.CourseRUD.as_view()),
    path('<int:course_id>/lesson-list-create/', views.LessonListCreate.as_view()),
    path('<int:course_id>/lesson-rud/<int:pk>/', views.LessonRUD.as_view()),
    path('<int:course_id>/lessons/<int:lesson_id>/lesson-file-list-create/', views.LessonFilesListCreate.as_view()),
    path('<int:course_id>/lessons/<int:lesson_id>/lesson-file-rud/<int:pk>/', views.LessonFilesRUD.as_view()),
    path('my-course/', views.MyCourseListCreate.as_view()),


]
