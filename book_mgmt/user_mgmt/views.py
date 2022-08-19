from distutils.command.clean import clean
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user_mgmt.forms import SignUpForm
# Create your views here.
User = get_user_model()


class RegisterView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'main_pages/auth-sign-up.html'
    success_url = reverse_lazy('books:homepage')    # TODO: make success url redirect to login page by yourself
    
    def get(self, request, *args, **kwargs):
        
        form = SignUpForm()
        return render(request, self.template_name, context={'form':form})
    
    
    # OR, use form_valid method instead of post
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            username = cleaned_data.get('username')
            email = cleaned_data.get('email')
            password = cleaned_data.get('password')
            
            user = User.objects.create(username=username, email=email, need_pwd_change=True, is_active=False)
            
            user.set_password(password) 
            user.save()
            
            # TODO: send template email by yourself
            
        return redirect('books:homepage')       #TODO: Redirect to login page by yourself
          