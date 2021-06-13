from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from .views import form_repuesto, home, form_mod_repuesto

urlpatterns = [
    path('',home,name='home'),
    path('form-repuesto',form_repuesto,name='form_repuesto'),
    path('form-mod-repuesto/<id>',form_mod_repuesto,name='form_mod_repuesto'),
=======
from .views import home

urlpatterns = [
    path('',home,name='home')
>>>>>>> parent of b967b03 (Incorporación form)
=======
from .views import home

urlpatterns = [
    path('',home,name='home')
>>>>>>> parent of b967b03 (Incorporación form)
=======
from .views import home

urlpatterns = [
    path('',home,name='home')
>>>>>>> parent of b967b03 (Incorporación form)
]