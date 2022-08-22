from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from user_mgmt.forms import SignUpForm, UserLoginForm

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


class LoginUserView(View):
    template_name = 'main_pages/login.html'

    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")

        return render(request, self.template_name, context={'form':self.form_class()})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                            password=form.cleaned_data.get('password'))

            if user is not None:
                # if user.need_password_change:
                #     login(self.request, user)
                #     return redirect('set_staff_password')
                if user.is_staff:
                    login(self.request, user)
                    next_url = self.request.GET.get('next')
                    if next_url:
                        return redirect(next_url)
                    return redirect('books:homepage')
                if not user.is_staff:
                    next_url = self.request.GET.get('next')
                    login(self.request, user)
                    if next_url:
                        return redirect(next_url)
                    return redirect('/')
                    
            else:
                messages.error(self.request, 'Invalid login credentials')


        return render(request, self.template_name, context={'form':form})


class UserLogoutView(LogoutView):
    # Use if redirecting to any customer default index page
    # next_page = reverse_lazy('/')
    template_name = 'main_pages/dashboard.html'
    