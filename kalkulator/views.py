from django.shortcuts import render
from .models import Racun, Vnos
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from kalkulator.models import Racun


def registracija(request):		
	return render(request, 'kalkulator/registracija.html')
	
def RegistracijaPodrobno(request):

	ime = request.GET['ime']
	geslo = request.GET['geslo']
	email = request.GET['email']
		
	a = User.objects.create_user(username=ime, password=geslo, email=email)
	a.save()	

	b = Racun.objects.create(ime="transakcijski racun", uporabnik=a, stanje=0 )
	b.save()
		
	context = {}
	racuni = Racun.objects.all()		
	context['racuni'] = racuni	
	
	login(request, a)
	
	context = {}
	racuni = Racun.objects.all()		
	context['racuni'] = racuni	

	return render(request, 'kalkulator/stanje.html', context)
	
def stanje(request):	 
	context = {}
	racuni = Racun.objects.all()		
	context['racuni'] = racuni		
	return render(request, 'kalkulator/stanje.html', context)
	
def StanjePodrobno(request):	
    context = {}     
    racuni = Racun.objects.all()	
    context['racuni'] = racuni	 
  
    answer = request.GET['dropdown'] 
    racun1 = Racun.objects.get(ime=answer, uporabnik=request.user)
    vnosi = Vnos.objects.filter(racun=racun1)
    context['vnosi'] = vnosi  
  
    sum = 0;    
    for vnos in vnosi:
   	    sum = sum + vnos.znesek		  
    context['vsota'] = sum  
  
    return render(request, 'kalkulator/StanjePodrobno.html', context)
 		
def vpisiPrihodek(request):
	context = {}     
	racuni = Racun.objects.all()		
	context['racuni'] = racuni	
	return render(request, 'kalkulator/vpisiPrihodek.html', context)
	
def vpisiPrihodekPodrobno(request):

	kategorija = request.GET['kategorija'] 
	racun = request.GET['racun']
	znesek = request.GET['znesek']
	podrobnosti = request.GET['podrobnosti']

	context = {}
	context['kategorija'] = kategorija
	context['racun'] = racun
	context['znesek'] = znesek
	context['podrobnosti'] = podrobnosti
	
	racun = Racun.objects.get(uporabnik=request.user, ime=racun)
	
	a = Vnos(kategorija=kategorija, znesek=znesek, podrobnosti=podrobnosti, vrsta="prihodek", racun=racun)	
	a.save()	
	
	racuni = Racun.objects.all()		
	context['racuni'] = racuni	
	
	return render(request, 'kalkulator/vpisiPrihodekPodrobno.html', context)	
	
	
def vpisiOdhodek(request):
	context = {}     
	racuni = Racun.objects.all()		
	context['racuni'] = racuni	
	return render(request, 'kalkulator/vpisiOdhodek.html', context)
	
def vpisiOdhodekPodrobno(request):
	context = {}
	
	kategorija = request.GET['kategorija'] 
	racun = request.GET['racun']
	znesek = request.GET['znesek']
	podrobnosti = request.GET['podrobnosti']
		
	znesek = int(znesek) * -1
	
	racun = Racun.objects.get(uporabnik=request.user, ime=racun)
	
	a = Vnos(kategorija=kategorija, znesek=znesek, podrobnosti=podrobnosti, vrsta="odhodek", racun=racun)	
	a.save()	
	
	racuni = Racun.objects.all()		
	context['racuni'] = racuni		
	
	return render(request, 'kalkulator/vpisiOdhodekPodrobno.html', context)
	
	
def porocila(request):
	context = {}
	
	racuni = Racun.objects.all()		
	context['racuni'] = racuni	
	
	return render(request, 'kalkulator/porocila.html', context)
	
def PorocilaPodrobno(request):
	context = {}
	
	kategorija = request.GET['kategorija'] 
	racun = request.GET['racun']
	
	racuni = Racun.objects.all()		
	context['racuni'] = racuni		
	
	racun = Racun.objects.get(uporabnik=request.user, ime=racun)
	
	vnosi = Vnos.objects.filter(racun=racun, kategorija=kategorija)
	
	context['vnosi'] = vnosi     
	
	sum = 0;    
	for vnos in vnosi:
		sum = sum + vnos.znesek
	
	context['vsota'] = sum   	
	
	return render(request, 'kalkulator/porocilaPodrobno.html', context)
	
def racun_prikazi(request):	
	return render(request, 'kalkulator/stanje.html', context)
		

  
  