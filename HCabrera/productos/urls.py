from django.urls import path
from .views import form_repuesto, home

urlpatterns = [
    path('',home,name='home'),
    path('form-repuesto',form_repuesto,name='form_repuesto'),
]