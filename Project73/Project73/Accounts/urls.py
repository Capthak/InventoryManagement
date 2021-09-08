from django.urls import path 
from .views import login_view,logout_view,register_view,changepass_view


urlpatterns=[
    path('Login/',login_view,name='LOGIN'),
    path('Logout/',logout_view,name='LOGOUT'),
    path('reg/',register_view,name='reg'),
    path('change/',changepass_view,name='CHANGE'),
    
]