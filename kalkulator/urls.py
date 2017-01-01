""" i created this """

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
	
	# login, logout
	url(r'^$', auth_views.login, {'template_name': 'kalkulator/login.html'}, name='login'),
	url(r'^login.html', auth_views.login, {'template_name': 'kalkulator/login.html'}, name='login'),			
	url(r'^logout/$', auth_views.logout, {'next_page': '/kalkulator'}, name='logout'),
	
	#	registracija
	url(r'^registracija', views.registracija, name='registracija'),
	url(r'^RegistracijaPodrobno', views.RegistracijaPodrobno, name='RegistracijaPodrobno'),		
		
	# stanje		
	url(r'^stanje', views.stanje, name='stanje'), 
	url(r'^StanjePodrobno', views.StanjePodrobno, name='StanjePodrobno'), 
	
	# vpisi prihodek
	url(r'^vpisiPrihodek', views.vpisiPrihodek, name='vpisiPrihodek'),
	url(r'^VpisiPrihodekPodrobno', views.vpisiPrihodekPodrobno, name='vpisiPrihodekPodrobno'), 
	
	# vpisi odhodek
	url(r'^vpisiOdhodek', views.vpisiOdhodek, name='vpisiOdhodek'),
	url(r'^VpisiOdhodekPodrobno', views.vpisiOdhodekPodrobno, name='vpisiOdhodekPodrobno'), 
	
	# porocila
	url(r'^porocila', views.porocila, name='porocila'),	
	url(r'^PorocilaPodrobno', views.PorocilaPodrobno, name='porocilaPodrobno'), 
	
]

