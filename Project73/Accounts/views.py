from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def register_view(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LOGIN')
    template_name='Register.html'
    context={'form':form}
    return render(request,template_name,context)


def login_view(request):
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('pword')
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user=user)
            return redirect('show')
        else:
            messages.error(request,'Invalid Credentials')
    template_name='Login.html'
    context={}
    return render(request,template_name,context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def changepass_view(request):
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('pword')
        new=request.POST.get('new_pword')
        con=request.POST.get('con_pword')
        user=authenticate(username=u,password=p)
        if user  and new==con:
            usr=User.objects.get(username=u)
            co=str(con)
            usr.set_password(co)
            usr.save()
            return redirect('LOGIN')
        else:
            messages.error(request,'PlEASE enter corect credentials')
    template_name="Change.html"
    context={}
    return render(request,template_name,context)


        





