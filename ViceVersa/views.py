from django.http import HttpResponse
from django.shortcuts import render


def about(request):
	return HttpResponse('This is about page')

def home(request):
	return render(request, 'home.html', {'greetiing':'Hello'})

def reverse(request):
	test_get_text = request.GET['usertext']
	newstring = test_get_text[::-1]

	print(newstring)
	return render(request, 'reverse.html', {'new_user_text':newstring, 'old_user_text':test_get_text})	

