from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Create your views here.
def index(request):
   # context_dict = {'boldmessage': "I am bold font from the context"}
   # return HttpResponse("Rango says hey there world! <br/><a href='/rango/about'>About</a>")
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page <br/><a href='/rango/'>Index</a>")
 
