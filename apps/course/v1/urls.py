from django.urls import path
# from .views import course_views, course_single
from .views import CourseListView, CourseDetailView, course_lesson

urlpatterns = [
    # path('courses/', course_views, name='courses'),
    # path('course_single/', course_single, name='course_single'),
    path('', CourseListView.as_view(), name='course_list'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('detail/<int:course_id>/lesson/<int:pk>/', course_lesson, name='course_lesson'),
]

