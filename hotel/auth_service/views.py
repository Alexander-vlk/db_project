from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


class RegisterView(CreateView):
    """View регистрации пользователей"""
    
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('admin:index')
    
    def form_valid(self, form):
        result = super().form_valid(form)
        data = form.cleaned_data
        
        user = authenticate(
            username=data['username'],
            password=data['password1'],
        )
        
        login(self.request, user)
        
        return result
