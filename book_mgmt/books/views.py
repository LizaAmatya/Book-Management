from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
# class HomePageView(View):
    
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("This is HelloWorld")
    
class HomePageView(TemplateView):
    
    template_name = "main_pages/dashboard.html"
    