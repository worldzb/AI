from django.http import HttpResponse
from django.shortcuts import render
# def hello(request):
#     return HttpResponse("Hello worldzb ! ")

def hello(request):
    context          = {}
    context['hello'] = 'Hello Worldzb!'
    context['a']=[1,2,12,12]
    return render(request, 'hello.html', context);

def test():
	pass

def haha():
	pass