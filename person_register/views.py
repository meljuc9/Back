from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import PersonForm
from serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):

	queryset = User.objects.all().order_by('_date_joined')
	serializer_class =UserSerializer

def home(request):
	persons = Person.objects.all()
	context = {'persons':persons}
	return render(request, 'person_register/dashboard.html', context)

def createPerson(request):
	form = PersonForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'person_register/person_form.html', context)

def updatePerson(request, pk):
	person = Person.objects.get(id=pk)
	form = PersonForm(instance=person)
	if request.method == 'POST':
		form = PersonForm(request.POST, instance=person)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'person_register/person_form.html', context)

def deletePerson(request, pk):
	person = Person.objects.get(id=pk)
	if request.method == "POST":
		person.delete()
		return redirect('/')
	context = {'person': person}
	return render(request, 'person_register/delete.html', context)