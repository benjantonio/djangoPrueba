from django.urls import path
from .views import form_repuesto, home, form_mod_repuesto, form_del_repuesto, panel_admin
urlpatterns = [
    path('',home,name='home'),
    path('panel-admin',panel_admin,name='panel_admin'),
    path('form-repuesto',form_repuesto,name='form_repuesto'),
    path('form-mod-repuesto/<id>',form_mod_repuesto,name='form_mod_repuesto'),
    path('form-del-repuesto/<id>',form_del_repuesto,name='form_del_repuesto'),
]