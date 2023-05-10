from django.urls import path
from .views import BlogView, BlogDetailView
from django.views.generic import TemplateView

urlpatterns = [
    # path('blog/', blog_views, name='blog'),
    # path('blog_single/', blog_single, name='blog_single'),
    # path('', TemplateView.as_view(template_name='blog/post_list.html'), name='blog'),
    path('', BlogView.as_view(), name='blog'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]

