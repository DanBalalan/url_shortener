from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('auth/', include('rest_auth.urls')),
]
