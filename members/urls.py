from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='members'),
    path('home/about/', views.about, name='about'),
    path('home/contact/', views.contact, name='contact'),
    path('home/men/', views.men, name='men'),
    path('home/women/', views.women, name='women'),
    path('details/<detid>/', views.property, name='property'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
