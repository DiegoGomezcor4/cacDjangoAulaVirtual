from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    
    path('acounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('acounts/logot/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    
    
    path('alumnos/listado', views.alumnos_listado, name='alumnos_listado'),
    path('alumnos/detalle/<str:nombre_alumno>', views.alumnos_detalle, name='alumnos_detalle'),
    re_path(r'alumnos/historico/(?P<year>[0-9]{4})/$', views.alumnos_historico, name='alumnos_historico'),
    path("alumnos/activos", views.alumnos_estado, {'estado': 'activo'}, name="alumnos_activos"),
    path("alumnos/inactivos", views.alumnos_estado, {'estado': 'inactivo'}, name="alumnos_inactivos"),
    path("alumnos/detalle/activos/<str:nombre_alumno>", views.alumnos_detalle_activos,name='alumnos_detalle_activos'),
    path('contacto',views.contacto, name='contacto'),
    path('alumnos/alta',views.alta_alumno,name='alta_alumno'),
    
    path('docentes/alta',views.DocenteCreateView.as_view(), name='alta_docente'),
    path('docentes/listado', views.DocenteListView.as_view(), name='docentes_listado'),
    
] 