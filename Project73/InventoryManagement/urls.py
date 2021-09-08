from django.urls import path
from .views import addOrder_view,showOrder_view,update_view,delete_view,home_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('show/', showOrder_view, name='show'),
    path('add/', addOrder_view, name='add'),
    path('update/<int:pk>', update_view, name='update'),
    path('delete/<int:pk>', delete_view, name='delete'),

]