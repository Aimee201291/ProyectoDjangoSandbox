from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
        MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

app_name = 'mascota'

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    #url(r'^nuevo$', mascota_view, name='mascota_crear'), #Cuando haga la petición a la url, va a ejecutar la vistas mascota_view
    #url(r'^listar', mascota_list, name='mascota_listar'),
    url(r'^listar', MascotaList.as_view(), name='mascota_listar'),#Como MascotaList es una clase, debemos indicar con el método as_view que se va a ejecutar como una vista
    #url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    #url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),

]
