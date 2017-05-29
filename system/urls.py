"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from accounts.views import UserRegisterView
from app import views
from app.views import usuarioDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^nosotros/', views.info, name='nosotros'),
    url(r'^app/', views.appinfo, name='appinfo'),
    url(r'^perfil/', views.userpag, name='perfil'),
    url(r'^usuario/(?P<pk>\d+)/$', usuarioDetailView.as_view(), name='usuario'),
    url(r'^usuario/(?P<slug>[\w-]+)/$', usuarioDetailView.as_view(), name='usuario_slug'),
    url(r'^registrar/$', UserRegisterView.as_view(), name='Registro'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^detalle/(?P<object_id>\d+)/$', views.detalle, name='detalle'),
]
