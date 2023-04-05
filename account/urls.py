from django.contrib import admin
from django.urls import path, include
from account.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from ProyectoCoder34675 import settings

urlpatterns = [
    path("editar/usuario", editar_usuario, name="accountEditarUsuario"),
    path("login/", login_account, name="accountLogin"),
    path("registrar/", register_account, name="accountRegistrar"),
    path("logout/", LogoutView.as_view(template_name="account/logout.html"), name="accountLogout")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)