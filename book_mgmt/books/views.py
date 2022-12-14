from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from user_mgmt.permissions import BookManagementPermission

from books.forms import BookForm
from books.models import Author, Book
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
class BookCreateView(LoginRequiredMixin, BookManagementPermission, CreateView):
    model = Book
    form_class = BookForm
    template_name = "main_pages/book_create.html"
    success_url = reverse_lazy('books:book_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['authors'] = Author.objects.all()

        return context
    
    def form_valid(self, form):
        obj = form.save()
        return super().form_valid(form)
    
    
class BookUpdateView(LoginRequiredMixin,BookManagementPermission, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "main_pages/book_edit.html"
    success_url = reverse_lazy('books:book_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['authors'] = Author.objects.all()

        return context
    