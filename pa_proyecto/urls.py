from django.conf.urls import include, url
from django.contrib import admin
from login.views import *
from django.contrib.auth.views import login
from django.contrib.auth import authenticate
from login.views import *

urlpatterns = [
        
   
    url(r'^home/$', home),
    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register), 
    url(r'^register/success/$', register_success),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/$', mapa), 

]
