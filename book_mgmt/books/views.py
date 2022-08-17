from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Book

# Create your views here.
# class HomePageView(View):
    
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("This is HelloWorld")
    
class HomePageView(TemplateView):
    
    template_name = "main_pages/dashboard.html"
    
    
class BookListView(ListView):
    template_name = "main_pages/book_list.html"
    queryset = Book.objects.all()
    context_object_name = "book_list"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'description':"this is test descriptions"})
        
        return context