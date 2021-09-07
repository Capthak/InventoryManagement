from django import forms
from .models import Product


class ProducModelForm(forms.ModelForm):

    class Meta:
        model=Product
        fields="__all__"
        widgets={
            'date':forms.SelectDateWidget()
        }
     

    
    


