from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('empresas/<str:nome_empresa>/addprod', views.addprod,  name='add_produto'),
    path('empresas/<str:nome_empresa>/addimg', views.addimg, name='add_img'),
    path('criar-usuario', views.criar_usuario, name='criar_user'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('criar-empresa', views.criar_empresa, name='criar_emp'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)