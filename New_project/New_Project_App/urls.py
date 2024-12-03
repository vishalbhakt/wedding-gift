from django.urls import re_path as url
from . import views

urlpatterns=[
 url(r'^$',views.main,name='main'),
 url(r'^aboutUs',views.aboutUs,name='aboutUs'),
 url(r'^signup', views.main, name = 'sign up'),
 url(r'^login', views.loginUser, name = 'login'),
 url(r'^register', views.registerUser, name = 'register'),
 url(r'^logout', views.logoutUser, name = 'logout'),
 url(r'^insert',views.insert,name='insert'),
 url(r'^services', views.services, name= "services" ),
 url(r'^invitation', views.invitation, name= "invitation" ),
 url(r'^couplestory', views.couplestory, name= "couple" ),
]