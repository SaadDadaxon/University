from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('v1/', include('apps.blog.v1.urls')),

    # api
    path('api/', include('apps.blog.api.urls'))
]
