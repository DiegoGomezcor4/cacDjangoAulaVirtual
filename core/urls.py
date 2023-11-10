from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/listado', views.alumnos_listado, name='alumnos_listado'),
    path('alumnos/detalle/<str:nombre_alumno>', views.alumnos_detalle, name='alumnos_detalle'),
    re_path(r'alumnos/historico/(?P<year>[0-9]{4})/$', views.alumnos_historico, name='alumnos_historico'),
    path("alumnos/activos", views.alumnos_estado, {'estado': 'activo'}, name="alumnos_activos"),
    path("alumnos/inactivos", views.alumnos_estado, {'estado': 'inactivo'}, name="alumnos_inactivos"),
    path("alumnos/detalle/activos/<str:nombre_alumno>", views.alumnos_detalle_activos,name='alumnos_detalle_activos'),
    path('contacto',views.contacto, name='contacto'),
    path('alumnos/alta',views.alta_alumno,name='alta_alumno')
] 