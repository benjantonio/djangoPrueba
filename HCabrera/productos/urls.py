from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from .views import form_repuesto, home, form_mod_repuesto
=======
from .views import form_repuesto, home
>>>>>>> parent of 8a155c2 (Modificación diseño tabla y creación mod_form)
=======
from .views import form_repuesto, home, form_mod_repuesto
>>>>>>> parent of f2cfc5d (Modificación html formulario)

urlpatterns = [
    path('',home,name='home'),
    path('form-repuesto',form_repuesto,name='form_repuesto'),
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> parent of 8a155c2 (Modificación diseño tabla y creación mod_form)
=======
    path('form-mod-repuesto/<id>',form_repuesto,name='form_mod_repuesto'),
    
>>>>>>> parent of f2cfc5d (Modificación html formulario)
]