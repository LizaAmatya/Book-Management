from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm  

User = get_user_model()


# can use UserCreationForm as well which provides regitration form : username. pwd
class SignUpForm(forms.ModelForm):
    password2 = forms.CharField(max_length=255)
    
    class Meta:
        model = User
        fields = ['username','email','password', 'password2']
    
    def clean(self):
        cleaned_data = super().clean()
        
        pwd1 = self.data.get('password')
        pwd2 = self.data.get('password2')
        
        if pwd1 != pwd2:
            raise forms.ValidationError("Password didnot match")
        
        return cleaned_data
    
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 20 or len(username) < 6:
            raise forms.ValidationError('Username should be 6-20 characters long.')

        if User.objects.filter(username__iexact=self.cleaned_data['username']).exists():
            raise forms.ValidationError('Username Exists')

        return username

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data.get('email')).exists():
            raise forms.ValidationError('Email Already Registered')
        return self.cleaned_data.get('email')
    