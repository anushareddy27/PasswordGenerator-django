from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
	return render(request, 'generator/home.html')
def about(request):
	return render(request, 'generator/about.html')
def password(request):

	characters=list('')

	if request.GET.get('uc'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('lc'):
		characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
	if request.GET.get('sc'):
		characters.extend(list('~!@#$%^&*()'))
	if request.GET.get('n'):
		characters.extend(list('0123456789'))

	le=int(request.GET.get('lengths'))
	passs=""
	for x in range(le):
		passs +=random.choice(characters)
	return render(request, 'generator/password.html', {'passw':passs})
