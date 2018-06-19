from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
	if action in request.GET:	
		action = request.GET['action']
	if action == 'load' :
		return HttpResponse('{"id1":{ "ttype": "ttype-1", "icode": "BDE43B34BE3", "desc": "Great Britain  adfasdfasdfadfasd", "bcode":"135670"}, "id2":{ "ttype": "ttype-2", "icode": "2343423ERWER", "desc": "Great Britain2 asdfadfasdfasdf", "bcode":"235670"}, "id3":{ "ttype": "ttype-3", "icode": "FGFG343434", "desc": "asdfadfasdf Great Britain3", "bcode":"345670"}, "id4":{ "ttype": "ttype-4", "icode": "_____FGFG343434", "desc": "___ Great Britain3 ___", "bcode":"345670"}}')
	elif action == 'save' :
		return HttpResponse('ok')




def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
