from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
    """View главной страницы"""
    
    template_name = 'registry/main_page.html'
