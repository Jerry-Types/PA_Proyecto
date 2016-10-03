from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
import folium



@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form':form})
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def mapa(request):
    print "Mandar Mapa"
    map_osm = folium.Map(location=[45.5236, -122.6750])
    map_osm.create_map(path='/home/nemis/pa_proyecto/login/templates/map/osm.html')
    return render_to_response(
    'map/osm.html',
    )
 
def logout_page(request):
    auth.logout(request)
    return HttpResponseRedirect("/home/")
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
)
