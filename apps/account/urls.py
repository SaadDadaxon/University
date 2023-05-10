from django.urls import path, include

app_name = 'account'

urlpatterns = [
    path('v1/', include('apps.account.v1.urls')),

    # api
    path('api/', include('apps.account.api.urls')),
]
