from django.urls import path

from registry.views import MainPageView, AboutUsView, PricesView, RoomsView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('prices/', PricesView.as_view(), name='prices'),
    path('rooms/', RoomsView.as_view(), name='rooms'),
    path('about/', AboutUsView.as_view(), name='about'),
]
