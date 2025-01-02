from django.urls import path

from auth_service.views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
