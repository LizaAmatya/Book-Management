from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['name', 'published_date', 'price', 'author', 'cover_image']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    # Teach for validation
    
    # def clean(self):
    #     cleaned_data = super(BookForm, self).clean()
    
    #     return cleaned_data
    
    # def clean_published_date(self):
    #     data = self.cleaned_data['published_date']
       
    #     # Logic here 
        
    #     # raise ValidationError("............")

    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return data
    