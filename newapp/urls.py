from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main_page/', views.main_page, name='main_page'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

