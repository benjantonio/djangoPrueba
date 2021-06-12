from django.urls import path
from .views import form_repuesto, home, form_mod_repuesto, form_del_repuesto

urlpatterns = [
    path('',home,name='home'),
    path('form-repuesto',form_repuesto,name='form_repuesto'),
    path('form-mod-repuesto/<id>',form_mod_repuesto,name='form_mod_repuesto'),
    path('form-del-repuesto/<id>',form_del_repuesto,name='form_del_repuesto'),
]