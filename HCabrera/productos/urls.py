from django.urls import path
from .views import form_repuesto, home, form_mod_repuesto

urlpatterns = [
    path('',home,name='home'),
    path('form-repuesto',form_repuesto,name='form_repuesto'),
    path('form-mod-repuesto/<id>',form_repuesto,name='form_mod_repuesto'),
    
]