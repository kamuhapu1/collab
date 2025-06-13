from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

