from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from alt import views
from cotizador import views as co
from django.conf.urls.static import static
from django.conf import settings
#from django.conf.urls import handler404
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^contacto/', views.contact, name='contact'),
	url(r'^empleo/', views.job, name='job'),
    url(r'^electronica/', views.electronica, name='electronica'),
    url(r'^vision/', views.vision, name='vision'),
    url(r'^termografia/', views.termografia, name='termografia'),
    url(r'^instrumentacion/', views.instrumentacion, name='instrumentacion'),
    url(r'^proyectos/trazabilidad/', views.proyecto_traza, name='proyecto_trazabilidad'),
    url(r'^proyectos/campana/', views.proyecto_campana, name='proyecto_campana'),
    url(r'^proyectos/monitorizacion/', views.proyecto_monitorizacion, name='proyecto_monitorizacion'),
    url(r'^proyectos/oximetro/', views.proyecto_oximetro, name='proyecto_oximetro'),
    url(r'^proyectos/ditek/', views.proyecto_ditek, name='proyecto_ditek'),
    url(r'^proyectos/localizador/', views.proyecto_localizador, name='proyecto_localizador'),
    url(r'^proyectos/medidor/', views.proyecto_medidor, name='proyecto_medidor'),
    url(r'^proyectos/', views.proyectos, name='proyectos'),
	url(r'^thermogenius/', views.thermogenius, name='thermogenius'),
    url(r'^admin/', admin.site.urls, name='dashboard'),
    url(r'^cotizador/', co.cotizador, name='cotizador'),
	url(r'^get/cotizador/', co.get_cotizador, name='get.cotizador'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
