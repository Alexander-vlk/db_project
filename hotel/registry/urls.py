from django.urls import path

from registry.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
]
