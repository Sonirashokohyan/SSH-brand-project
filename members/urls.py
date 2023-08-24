from django.urls import path
from . import views

urlpatterns = [
    # path('', views.members, name='members'),
    path('members/', views.members, name='members'),
    path('members/index', views.index, name='index'),
    path('members/index/shop', views.shop, name='shop'),
    path('members/index/about', views.about, name='about'),
    path('members/index/contact', views.contact, name='contact'),
    path('members/index/men', views.men, name='men'),
    path('members/index/women', views.women, name='women'),
    path('members/details/<int:id>', views.details, name='details'),

    # path('members/sonira', views.sonira, name='members.sonira'),
    # path('members/fariha', views.fariha, name='members.fariha'),
    # path('members/freshta', views.freshta, name='members.freshta'),
    # path('members/maryam', views.maryam, name='members.maryam'),
    # path('members/khujesta', views.khujesta, name='members.khujesta'),
    # path('members/karima', views.karima, name='members.karima'),
    # path('members/mursal', views.mursal, name='members.mursal'),
    # path('members/nazanin', views.nazanin, name='members.nazanin'),
    # path('members/zahra', views.zahra, name='members.zahra'),
    # path('members/frohar', views.frohar, name='members.frohar'),
]