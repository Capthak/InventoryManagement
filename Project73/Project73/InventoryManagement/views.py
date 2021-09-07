
from django import forms
from django.shortcuts import render,redirect
from .models import Product
from .forms import ProducModelForm

def addOrder_view(request):
    form=ProducModelForm()
    if request.method=='POST':
        form=ProducModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='AddOrder.html'
    context={'form':form}
    return render(request,template_name,context)

def showOrder_view(request):
    obj=Product.objects.all()
    print(obj)
    template_name='ShowOrder.html'
    context={'obj':obj}
    return render(request,template_name,context)

def update_view(request,pk):
    obj=Product.objects.get(id=pk)
    form=ProducModelForm(instance=obj)
    if request.method=='POST':
        form=ProducModelForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='AddOrder.html'
    context={'form':form}
    return render(request,template_name,context)

def delete_view(request,pk):
    obj=Product.objects.get(id=pk)
    obj.delete()
    return redirect('show')

def home_view(request):
    template_name='Home.html'
    context={}
    return render(request,template_name,context)


    



        
