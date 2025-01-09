from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
    """View главной страницы"""
    
    template_name = 'registry/main_page.html'


class PricesView(TemplateView):
    """View цен"""
    
    template_name = 'registry/prices.html'


class RoomsView(TemplateView):
    """View номеров отеля"""
    
    template_name = 'registry/rooms.html'


class AboutUsView(TemplateView):
    """View страницы о нас"""
    
    template_name = 'registry/about_us.html'
