from django.shortcuts import render



def index(request):

	return render(request, 'kalkulator/index.html')


	#return HttpResponse("<h1>This is the kalkulator app homepage")

# Create your views here.
